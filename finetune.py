import os
import sys
import glob
import argparse
from typing import List

import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer
from datasets import load_dataset, concatenate_datasets, DatasetDict

from peft import (
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
    prepare_model_for_int8_training,
    set_peft_model_state_dict,
)

from utils.prompter import Prompter


def parse_args():
    parser = argparse.ArgumentParser()
    # Model & Data
    parser.add_argument("--base_model", type=str, help="Path to pretrained model", required=True)
    parser.add_argument("--data_path", type=str, default="MBZUAI/Bactrian-X", help="Data path to a local file/folder, or 'MBZUAI/Bactrian-X' Dataset Hub.")
    parser.add_argument("--lang", type=str, default="", help="Language codes separated by comma (only if you want to fetch data from Hugging Face Dataset Hub).")
    parser.add_argument("--output_dir", type=str, default="output")
    parser.add_argument("--template_dir", type=str, default="./templates")
    parser.add_argument("--prompt_template_name", type=str, default="bactrian")
    # Training
    parser.add_argument("--batch_size", type=int, default=128)
    parser.add_argument("--micro_batch_size", type=int, default=32)
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--learning_rate", type=float, default=1e-4)
    parser.add_argument("--cutoff_len", type=int, default=512)
    parser.add_argument("--val_set_size", type=int, default=1000)
    parser.add_argument("--logging_steps", type=int, default=50)
    parser.add_argument("--eval_steps", type=int, default=500)
    parser.add_argument("--save_steps", type=int, default=500)
    parser.add_argument("--resume_from_checkpoint", type=str, default=None)
    # Lora
    parser.add_argument("--lora_r", type=int, default=8)
    parser.add_argument("--lora_alpha", type=int, default=16)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--lora_target_modules", type=str, default="q_proj,v_proj")
    # LLM
    parser.add_argument("--train_on_inputs", action='store_true')
    parser.add_argument("--add_eos_token", action='store_true')
    parser.add_argument("--group_by_length", action='store_true')
    # Logging
    parser.add_argument("--use_wandb", action='store_true')
    parser.add_argument("--push_to_hub", action='store_true') # TODO

    args = parser.parse_args()
    return args

def train():
    args = parse_args()
    if int(os.environ.get("LOCAL_RANK", 0)) == 0:
        print(args)
    assert (args.base_model), "Please specify a --base_model, e.g. --base_model='decapoda-research/llama-7b-hf'"

    args.lora_target_modules = args.lora_target_modules.split(',')
    gradient_accumulation_steps = args.batch_size // args.micro_batch_size

    prompter = Prompter(args.prompt_template_name, args.template_dir)

    device_map = "auto"
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    ddp = world_size != 1
    if ddp:
        device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)}
        gradient_accumulation_steps = gradient_accumulation_steps // world_size

    model = LlamaForCausalLM.from_pretrained(
        args.base_model,
        load_in_8bit=True,
        torch_dtype=torch.float16,
        device_map=device_map,
    )

    tokenizer = LlamaTokenizer.from_pretrained(args.base_model)

    tokenizer.pad_token_id = (
        0  # unk. we want this to be different from the eos token
    )
    tokenizer.padding_side = "left"  # Allow batched inference

    def tokenize(prompt, add_eos_token=True):
        # there's probably a way to do this with the tokenizer settings
        # but again, gotta move fast
        result = tokenizer(
            prompt,
            truncation=True,
            max_length=args.cutoff_len,
            padding=False,
            return_tensors=None,
        )
        if (
            result["input_ids"][-1] != tokenizer.eos_token_id
            and len(result["input_ids"]) < args.cutoff_len
            and add_eos_token
        ):
            result["input_ids"].append(tokenizer.eos_token_id)
            result["attention_mask"].append(1)

        result["labels"] = result["input_ids"].copy()

        return result

    def generate_and_tokenize_prompt(data_point):
        full_prompt = prompter.generate_prompt(
            data_point["instruction"],
            data_point["input"],
            data_point["output"],
        )
        tokenized_full_prompt = tokenize(full_prompt)
        if not args.train_on_inputs:
            user_prompt = prompter.generate_prompt(
                data_point["instruction"], data_point["input"]
            )
            tokenized_user_prompt = tokenize(
                user_prompt, add_eos_token=args.add_eos_token
            )
            user_prompt_len = len(tokenized_user_prompt["input_ids"])

            if args.add_eos_token:
                user_prompt_len -= 1

            tokenized_full_prompt["labels"] = [
                -100
            ] * user_prompt_len + tokenized_full_prompt["labels"][
                user_prompt_len:
            ]  # could be sped up, probably
        return tokenized_full_prompt

    model = prepare_model_for_int8_training(model)

    config = LoraConfig(
        r = args.lora_r,
        lora_alpha = args.lora_alpha,
        target_modules = args.lora_target_modules,
        lora_dropout = args.lora_dropout,
        bias = "none",
        task_type = "CAUSAL_LM",
    )
    model = get_peft_model(model, config)

    if args.data_path.endswith(".json"): # Load single local file
        all_dataset = [load_dataset("json", data_files=args.data_path)]
    elif args.lang != '': # Load multiple subset from Hugging Face Hub
        all_dataset = [load_dataset(args.data_path, lang) for lang in args.lang.split(',')]
    else: # Load multiple local file (all json files from a folder)
        all_dataset = [load_dataset("json", data_files=f) for f in glob.glob(os.path.join(args.data_path,'*.json'))]
    merged_dataset = concatenate_datasets(list(map(lambda x: x['train'], all_dataset)))
    data = DatasetDict({'train':merged_dataset})

    if args.resume_from_checkpoint:
        # Check the available weights and load them
        checkpoint_name = os.path.join(
            args.resume_from_checkpoint, "pytorch_model.bin"
        )  # Full checkpoint
        if not os.path.exists(checkpoint_name):
            checkpoint_name = os.path.join(
                args.resume_from_checkpoint, "adapter_model.bin"
            )  # only LoRA model - LoRA config above has to fit
            args.resume_from_checkpoint = (
                False  # So the trainer won't try loading its state
            )
        # The two files above have a different name depending on how they were saved, but are actually the same.
        if os.path.exists(checkpoint_name):
            print(f"Restarting from {checkpoint_name}")
            adapters_weights = torch.load(checkpoint_name)
            set_peft_model_state_dict(model, adapters_weights)
        else:
            print(f"Checkpoint {checkpoint_name} not found")

    model.print_trainable_parameters()  # Be more transparent about the % of trainable params.

    if args.val_set_size > 0:
        train_val = data["train"].train_test_split(
            test_size=args.val_set_size, shuffle=True, seed=42
        )
        train_data = (
            train_val["train"].shuffle().map(generate_and_tokenize_prompt)
        )
        val_data = (
            train_val["test"].shuffle().map(generate_and_tokenize_prompt)
        )
    else:
        train_data = data["train"].shuffle().map(generate_and_tokenize_prompt)
        val_data = None

    if not ddp and torch.cuda.device_count() > 1:
        # keeps Trainer from trying its own DataParallelism when more than 1 gpu is available
        model.is_parallelizable = True
        model.model_parallel = True

    trainer = transformers.Trainer(
        model = model,
        train_dataset = train_data,
        eval_dataset = val_data,
        args = transformers.TrainingArguments(
            per_device_train_batch_size = args.micro_batch_size,
            gradient_accumulation_steps = gradient_accumulation_steps,
            warmup_steps = 200,
            num_train_epochs = args.num_epochs,
            learning_rate = args.learning_rate,
            fp16 = True,
            logging_steps = args.logging_steps,
            optim = "adamw_torch",
            evaluation_strategy = "steps" if args.val_set_size > 0 else "no",
            save_strategy = "steps",
            eval_steps = args.eval_steps if args.val_set_size > 0 else None,
            save_steps = args.save_steps,
            output_dir = args.output_dir,
            save_total_limit = 3,
            load_best_model_at_end = True if args.val_set_size > 0 else False,
            ddp_find_unused_parameters = False if ddp else None,
            group_by_length = args.group_by_length,
            report_to = "wandb" if args.use_wandb else None,
        ),
        data_collator = transformers.DataCollatorForSeq2Seq(
            tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True
        ),
    )
    model.config.use_cache = False

    old_state_dict = model.state_dict
    model.state_dict = (
        lambda self, *_, **__: get_peft_model_state_dict(
            self, old_state_dict()
        )
    ).__get__(model, type(model))

    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)

    trainer.train(resume_from_checkpoint = args.resume_from_checkpoint)

    model.save_pretrained(args.output_dir)

    print(
        "\n If there's a warning about missing keys above, please disregard :)"
    )


if __name__ == "__main__":
    train()
