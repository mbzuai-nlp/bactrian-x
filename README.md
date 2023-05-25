<h1 align="center"> <p>🐫 MBZUAI Bactrian-X</p></h1>
<h3 align="center">
    <p>A Multilingual Replicable Instruction-Following Model</p>
</h3>

<p align="center"> <a href="https://haonan-li.github.io/" target="_blank">Haonan Li</a>*, <a href="http://www.fajrikoto.com" target="_blank">Fajri Koto</a>*, <a href="https://twitter.com/WuMinghao_nlp" target="_blank">Minghao Wu</a>, <a href="https://afaji.github.io/" target="_blank">Alham Fikri Aji</a>, <a href="https://people.eng.unimelb.edu.au/tbaldwin/" target="_blank">Timothy Baldwin</a> (*equal contribution) </p>

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)


## :fire: News
<!---
-->
* **[2023.05.25]** The preprint of our paper is [here](https://arxiv.org/abs/2305.15011).
* **[2023.05.25]** Bactrian-X [llama-7b-lora](https://huggingface.co/MBZUAI/bactrian-x-llama-7b-lora), [llama-13b-lora](https://huggingface.co/MBZUAI/bactrian-x-llama-13b-lora), [bloom-7b1-lora](https://huggingface.co/MBZUAI/bactrian-x-bloom-7b1-lora) are available. 
* **[2023.04.22]** Release of data in 52 languages [here](https://huggingface.co/datasets/MBZUAI/Bactrian-X).

## Overview
<h3 align="center">
<img src="https://github.com/fajri91/eval_picts/blob/master/BactrianX_full.jpg" width="1000" align="center">
</h3>

**Bactrian-X dataset** contains 3.4M pairs of instructions and responses in 52 languages.
The instructions were obtained from [alpaca-52k](https://github.com/tatsu-lab/stanford_alpaca), and [dolly-15k](https://github.com/databrickslabs/dolly/tree/master/data), and tranlated into 52 languages (52 languages x 67k instances = 3.4M instances).
The responses in 52 languages were generated from `gpt-3.5-turbo` model.

**Bactrian-X models** are a series of LLM models fine-tuned (using [low-rank adaptation/LoRA](https://arxiv.org/pdf/2106.09685.pdf)) on Bactrian-X dataset. 

<!--
Specifically, this repository contains:

- The [67K instruction data](#data-and-model-release) in 52 languages.
- Multilingual [Bactrian-X](#data-and-model-release), trained on combined language-instruction pairs (3.4M instances).
- 52 monolingual Bactrian models, trained on each of the 52 languages (67k instances).
- The code for [training the model](#model-training-and-inference) using [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685.pdf).
-->

**Usage and License Notices**: Bactrian-X is intended and licensed for research use only. The dataset is CC BY NC 4.0 (allowing only non-commercial use) and models trained using the dataset should not be used outside of research purposes. 

### Dataset

We curate our [Bactrian instruction dataset](https://huggingface.co/datasets/MBZUAI/Bactrian-X) with the following steps:

1. **Collecting English instructions**: The English instructions are obtained from [alpaca-52k](https://github.com/tatsu-lab/stanford_alpaca) and [dolly-15k](https://github.com/databrickslabs/dolly/tree/master/data), and they are saved to [instructions.json](https://github.com/MBZUAI-nlp/Bactrian-X/data/instructions.json).
2. **Translating the English instructions into foreign languages**: The instructions (and the corresponding inputs, if any) are translated into 51 languages using the Google Translate API (conducted in April 2023).
3. **Generating the responses**: We generate output from `gpt-3.5-turbo` for the instructions in each language (conducted in April 2023).

<!--
we noticed that the performance of the languages that not covered by the original LLM pretraining may not satifactory.
So we recommand users to choose the model by considering whether the languages were covered.
The datasets, Bactrian-ISO code, and the LLM models langauge coverage were listed below.

| No | Languages       | Code and Data                                                               | LLaMA    | Bloom     |
| ---|---------------- | ------------------------------------------------------------------------    | ------   | --------- |
|  1 | Afrikaans       | [af_ZA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/af/train)  |          |           |
|  2 | Arabic          | [ar_AR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ar/train)  |          | &#x2713;  |
|  3 | Azerbaijani     | [az_AZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/az/train)  |          |           |
|  4 | Bengali         | [bn_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/bn/train)  |          |           |
|  5 | Czech           | [cs_CZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/cs/train)  | &#x2713; |           |
|  6 | German          | [de_DE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/de/train)  | &#x2713; |           |
|  7 | English         | [en_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/en/train)  | &#x2713; | &#x2713;  |
|  8 | Spanish         | [es_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/es/train)  | &#x2713; | &#x2713;  |
|  9 | Estonian        | [et_EE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/et/train)  |          |           |
| 10 | Persian         | [fa_IR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fa/train)  |          |           |
| 11 | Finnish         | [fi_FI](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fi/train)  |          |           |
| 12 | French          | [fr_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fr/train)  | &#x2713; | &#x2713;  |
| 13 | Galician        | [gl_ES](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/gl/train)  |          |           |
| 14 | Gujarati        | [gu_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/gu/train)  |          | &#x2713;  |
| 15 | Hebrew          | [he_IL](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/he/train)  |          |           |
| 16 | Hindi           | [hi_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/hi/train)  |          | &#x2713;  |
| 17 | Croatian        | [hr_HR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/hr/train)  | &#x2713; |           |
| 18 | Indonesian      | [id_ID](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/id/train)  |          | &#x2713;  |
| 19 | Italian         | [it_IT](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/it/train)  | &#x2713; |           |
| 20 | Japanese        | [ja_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ja/train)  |          |           |
| 21 | Georgian        | [ka_GE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ka/train)  |          |           |
| 22 | Kazakh          | [kk_KZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/kk/train)  |          |           |
| 23 | Khmer           | [km_KH](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/km/train)  |          |           |
| 24 | Korean          | [ko_KR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ko/train)  |          |           |
| 25 | Lithuanian      | [lt_LT](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/lt/train)  |          |           |
| 26 | Latvian         | [lv_LV](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/lv/train)  |          |           |
| 27 | Macedonian      | [mk_MK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mk/train)  |          |           |
| 28 | Malayalam       | [ml_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ml/train)  |          | &#x2713;  |
| 29 | Mongolian       | [mn_MN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mn/train)  |          |           |
| 30 | Marathi         | [mr_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mr/train)  |          | &#x2713;  |
| 31 | Burmese         | [my_MM](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/my/train)  |          |           |
| 32 | Nepali          | [ne_NP](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ne/train)  |          | &#x2713;  |
| 33 | Dutch           | [nl_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/nl/train)  | &#x2713; |           |
| 34 | Polish          | [pl_PL](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/pl/train)  | &#x2713; |           |
| 35 | Pashto          | [ps_AF](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ps/train)  |          |           |
| 36 | Portuguese      | [pt_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/pt/train)  | &#x2713; | &#x2713;  |
| 37 | Romanian        | [ro_RO](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ro/train)  | &#x2713; |           |
| 38 | Russian         | [ru_RU](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ru/train)  | &#x2713; |           |
| 39 | Sinhala         | [si_LK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/si/train)  |          |           |
| 40 | Slovene         | [sl_SI](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sl/train)  | &#x2713; |           |
| 41 | Swedish         | [sv_SE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sv/train)  | &#x2713; |           |
| 42 | Swahili         | [sw_KE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sw/train)  |          | &#x2713;  |
| 43 | Tamil           | [ta_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ta/train)  |          | &#x2713;  |
| 44 | Telugu          | [te_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/te/train)  |          | &#x2713;  |
| 45 | Thai            | [th_TH](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/th/train)  |          |           |
| 46 | Tagalog         | [tl_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/tl/train)  |          |           |
| 47 | Turkish         | [tr_TR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/tr/train)  |          |           |
| 48 | Ukrainian       | [uk_UA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/uk/train)  | &#x2713; |           |
| 49 | Urdu            | [ur_PK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ur/train)  |          | &#x2713;  |
| 50 | Vietnamese      | [vi_VN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/vi/train)  |          | &#x2713;  |
| 51 | Xhosa           | [xh_ZA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/xh/train)  |          | &#x2713;  |
| 52 | Chinese         | [zh_CN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/zh/train)  |          | &#x2713;  |
-->


### Models

With our dataset and [Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685), we present a family of multilingual and monolingual models based on [LLaMA](https://arxiv.org/abs/2302.13971) and [BLOOM](https://arxiv.org/abs/2211.05100).
Our instruction-tuned multilingual Bactrian-X models are available at: 
* [MBZUAI/bactrian-x-llama-7b-lora](https://huggingface.co/MBZUAI/bactrian-x-llama-7b-lora) 
* [MBZUAI/bactrian-x-llama-13b-lora](https://huggingface.co/MBZUAI/bactrian-x-llama-13b-lora)
* [MBZUAI/bactrian-x-bloom-7b1-lora](https://huggingface.co/MBZUAI/bactrian-x-bloom-7b1-lora)

**Note**: We are continually updating this repository. The number of languages will be more than 52 in the future, and the current models are mostly only 7B in size. We welcome any collaborators who are willing to contribute larger models.

## Hands-on Bactrian-X

### Setting up the Environment
```bash
conda create -n bactrian python=3.9
conda activate bactrian
pip install -r requirements.txt
```

### Training

Models are trained with the following hyperparameters:

| Hyper-parameter | Bactrian-X |
| --------------- | ---------- |
| batch_size      | 128        |
| num_epochs      | 10         |
| learning_rate   | 3e-4       |
| cutoff_len      | 768        |
| lora_r          | 64         |
| lora_alpha      | 16         |

Below is a command to train a LLaMA-7B adapter with our datasets in specific language(s). Replace `<lang_iso>` with a list of (one or more) ISO-639-2 language codes separated by commas (e.g., `en,zh` for `English` and `Chinese`), and `<your_output_dir>` to specify where to store the outputs.

```bash
# Script to train on 4x Nvidia A100 80GB gpus
WORLD_SIZE=4
CUDA_VISIBLE_DEVICES=0,1,2,3
torchrun --nproc_per_node=4 --master_port=1234 finetune_hf.py \
    --model_name_or_path decapoda-research/llama-7b-hf \
    --lang <lang_iso> \
    --output_dir <your_output_dir> \
    --per_device_train_batch_size 32 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --num_train_epochs 10 \
    --model_max_length 768 \
    --learning_rate 3e-4 \
    --val_set_size 2000 \
    --warmup_steps 200 \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q_proj,k_proj,v_proj,o_proj' \
    --group_by_length 
```

### Inference

This is example code that loads both the foundation model and Bactrian LoRA weights from the Hugging Face model hub, and runs a Gradio interface for inference on a specified input. 
```bash
python generate.py \
    --load_8bit \
    --base_model 'decapoda-research/llama-7b-hf' \
    --lora_weights 'MBZUAI/bactrian-x-llama-7b-lora' \
    --share_gradio 
```

### Checkpoint export 

To merge the LoRA weights back into the base model for export to Hugging Face format and to PyTorch `state_dicts`, go to [Alpaca-LoRA](https://github.com/tloen/alpaca-lora).
This should help users who want to run inference in projects like [llama.cpp](https://github.com/ggerganov/llama.cpp) or [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp).


## Output Examples 
Please check output examples [here](eval/README.md).

## Citation

Please cite the repo if you use the data, model or code in this repo. A paper will be released very soon.

```
@misc{li2023bactrianx,
      title={Bactrian-X : A Multilingual Replicable Instruction-Following Model with Low-Rank Adaptation}, 
      author={Haonan Li and Fajri Koto and Minghao Wu and Alham Fikri Aji and Timothy Baldwin},
      year={2023},
      eprint={2305.15011},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Naturally, you should also cite the original [LLaMA paper](https://arxiv.org/abs/2302.13971), the [Self-Instruct paper](https://arxiv.org/abs/2212.10560), and the [Stanford Alpaca repo](https://github.com/tatsu-lab/stanford_alpaca).

## Acknowledgements

We are standing on the shoulders of giants and would like to especially acknowledge the previous efforts of the following works.:

1. [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)
2. [Alpaca-LoRA](https://github.com/tloen/alpaca-lora)
3. [Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685)
4. [PEFT](https://github.com/huggingface/peft)
5. [LLM.int8()](https://arxiv.org/abs/2208.07339)
