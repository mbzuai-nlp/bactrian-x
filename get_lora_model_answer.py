import argparse
import torch
import os,sys
import json
from tqdm import tqdm
import shortuuid
# import ray
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaTokenizer, Trainer, GenerationConfig, LlamaForCausalLM
from peft import PeftModel

from data.__init__ import iso2lang
from utils.prompter import Prompter


def run_eval(args):
    # split question file into num_gpus files
    ques_jsons = []
    with open(args.question_file, "r") as ques_file:
        for line in ques_file:
            ques_jsons.append(line)

    chunk_size = len(ques_jsons) // args.num_gpus
    ans_handles = []
    for i in range(0, len(ques_jsons), chunk_size):
        ans_handles.append(
            #get_model_answers.remote(args, ques_jsons[i : i + chunk_size]
            get_model_answers(args, ques_jsons[i : i + chunk_size]
            )
        )

    ans_jsons = []
    for ans_handle in ans_handles:
        #ans_jsons.extend(ray.get(ans_handle))
        ans_jsons.extend(ans_handle)

    answer_directory = os.path.dirname(args.answer_file)
    if not os.path.exists(answer_directory):
        os.makedirs(answer_directory)

    with open(args.answer_file, "w",  encoding='utf-8') as ans_file:
        for line in ans_jsons:
            ans_file.write(json.dumps(line, ensure_ascii=False) + "\n")


# @ray.remote(num_gpus=1)
@torch.inference_mode()
def get_model_answers(args, question_jsons):

    prompter = Prompter(args.prompt_template_name, args.template_dir)
    # Todo: better handle
    tokenizer_class = LlamaTokenizer if 'llama' in args.base_model else AutoTokenizer
    model_class = LlamaForCausalLM if 'llama' in args.base_model else AutoModelForCausalLM

    tokenizer = tokenizer_class.from_pretrained(args.base_model)
    model = model_class.from_pretrained(
        args.base_model,
        load_in_8bit=args.load_8bit,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    if args.lora_weights:
        model = PeftModel.from_pretrained(
            model,
            args.lora_weights,
            torch_dtype=torch.float16,
        )

    # unwind broken decapoda-research config
    if 'llama' in args.base_model:
        model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
        model.config.bos_token_id = 1
        model.config.eos_token_id = 2

    if not args.load_8bit:
        model.half()


    ans_jsons = []
    for i, line in enumerate(tqdm(question_jsons)):
        ques_json = json.loads(line)
        idx = ques_json["question_id"]
        qs = ques_json["text"]
        # Todo: better handle
        lang = iso2lang[ques_json["lang"]] if args.prompt_template_name == 'alpaca_with_lang' else None

        prompt = prompter.generate_prompt(instruction=qs, input='', language=lang)
        inputs = tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].cuda()

        generation_config = GenerationConfig(
            temperature=0.1,
            no_repeat_ngram_size=3,
        )

        generate_params = {
            "input_ids": input_ids,
            "generation_config": generation_config,
            "return_dict_in_generate": True,
            "output_scores": True,
            "max_new_tokens": 1024,
        }
        with torch.no_grad():
            generation_output = model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=1024,
            )
        s = generation_output.sequences[0]
        outputs = tokenizer.decode(s)

        ans_id = shortuuid.uuid()
        # print(outputs)
        ans_jsons.append(
            {
                "question_id": idx,
                "text": outputs,
                "answer_id": ans_id,
                "metadata": {},
            }
        )
    return ans_jsons


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_model", type=str, help="Path to pretrained model", default="decapoda-research/llama-7b-hf")
    parser.add_argument("--load_8bit", action='store_true')
    parser.add_argument("--lora_weights", type=str)
    parser.add_argument("--template_dir", type=str, default="../templates")
    parser.add_argument("--prompt_template_name", type=str, default="bactrian")
    parser.add_argument("--question_file", type=str, required=True)
    parser.add_argument("--answer_file", type=str, default="answer.jsonl")
    parser.add_argument("--num_gpus", type=int, default=1)
    args = parser.parse_args()

    # ray.init()
    run_eval(args)
