<h1 align="center"> <p>🐫 MBZUAI Bactrian-X</p></h1>
<h3 align="center">
    <p>A Multilingual Replicable Instruction-Following Model</p>
</h3>

<p align="center"> <a href="https://haonan-li.github.io/" target="_blank">Haonan Li</a>*, <a href="http://www.fajrikoto.com" target="_blank">Fajri Koto</a>*, <a href="https://people.eng.unimelb.edu.au/tbaldwin/" target="_blank">Timothy Baldwin</a> (*equal contribution) </p>

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)


## :fire: News
<!---
-->
* **[2023.04.28]** 52-in-1 Bactrian-X model is now available [here](https://huggingface.co/MBZUAI/Bactrian-X).
* **[2023.04.24]** Monolingual models in 52 languages are released, and are available [here](https://huggingface.co/haonan-li).
* **[2023.04.22]** Data in 52 languages are released, and are available [here](https://huggingface.co/datasets/MBZUAI/Bactrian-X).


## Overview
<h3 align="center">
<img src="https://github.com/fajri91/eval_picts/blob/master/BactrianX_full.jpg" width="1000" align="center">
</h3>

Bactrian-X is a 7B multilingual model fine-tuned from the LLaMA 7B model (using [low-rank adaptation/LoRA](https://arxiv.org/pdf/2106.09685.pdf)) on 3.4M instruction-following demonstrations. The 3.4M instances are obtained from 52 languages of [alpaca-52k](https://github.com/tatsu-lab/stanford_alpaca), and [dolly-15k](https://github.com/databrickslabs/dolly/tree/master/data) (52 languages x 67k instances = 3.4M instances).

Specifically, this repository contains:

- The [67K instruction data](#data-and-model-release) in 52 languages.
- Multilingual [Bactrian-X](#data-and-model-release), trained on combined language-instruction pairs (3.4M instances).
- 52 monolingual Bactrian models, trained on each 52 languages (67k instances).
- The code for [training the model](#model-training-and-inference) using [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685.pdf).

**Usage and License Notices**: Bactrian-X is intended and licensed for research use only. The dataset is CC BY NC 4.0 (allowing only non-commercial use) and models trained using the dataset should not be used outside of research purposes. 


## Data and Model Release

**Note**: We are keep updating this repository. Number of languages will be more than 52 in future, and the current models are mostly only in 7B-size. We are welcome any researchers who want to contribute larger models.

Data preperation:

1. English Instructions: The English instuctions are obtained from [alpaca-52k](https://github.com/tatsu-lab/stanford_alpaca), and [dolly-15k](https://github.com/databrickslabs/dolly/tree/master/data), saved to [instructions.json](https://github.com/MBZUAI-nlp/Bactrian-X/data/instructions.json).
2. Instruction Translation: The instructions (and inputs) are translated into 51 languages using Google Translation API (conducted on April 2023).
3. Output Generation: We generate output from `gpt-3.5-turbo` for each language (conducted on April 2023).


We use 52 languages of [mBART-50](https://arxiv.org/abs/2008.00401). Each dataset, monolingual models (Bactrian-ISO), and multilingual model (Bactrian-X) can be downloaded below. 



| No | Languages       | Code and Data                                                               | Adapter (7B)                                                        | Adapter (13B)   |
| ---|---------------- | ------------------------------------------------------------------------    | ----------------------------------------------------------------    | --------------- |
|  0 | 52 languages    | X (Below)                                                                   | [Bactrian-X](https://huggingface.co/MBZUAI/bactrian-X-7b-lora)      |  |
|  1 | Afrikaans       | [af_ZA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/af/train)  | [Bactrian-af](https://huggingface.co/haonan-li/bactrian-af-7b-lora) |  |
|  2 | Arabic          | [ar_AR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ar/train)  | [Bactrian-ar](https://huggingface.co/haonan-li/bactrian-ar-7b-lora) |  |
|  3 | Azerbaijani     | [az_AZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/az/train)  | [Bactrian-az](https://huggingface.co/haonan-li/bactrian-az-7b-lora) |  |
|  4 | Bengali         | [bn_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/bn/train)  | [Bactrian-bn](https://huggingface.co/haonan-li/bactrian-bn-7b-lora) |  |
|  5 | Czech           | [cs_CZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/cs/train)  | [Bactrian-cs](https://huggingface.co/haonan-li/bactrian-cs-7b-lora) |  |
|  6 | German          | [de_DE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/de/train)  | [Bactrian-de](https://huggingface.co/haonan-li/bactrian-de-7b-lora) |  |
|  7 | English         | [en_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/en/train)  | [Bactrian-en](https://huggingface.co/haonan-li/bactrian-en-7b-lora) |  |
|  8 | Spanish         | [es_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/es/train)  | [Bactrian-es](https://huggingface.co/haonan-li/bactrian-es-7b-lora) |  |
|  9 | Estonian        | [et_EE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/et/train)  | [Bactrian-et](https://huggingface.co/haonan-li/bactrian-et-7b-lora) |  |
| 10 | Persian         | [fa_IR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fa/train)  | [Bactrian-fa](https://huggingface.co/haonan-li/bactrian-fa-7b-lora) |  |
| 11 | Finnish         | [fi_FI](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fi/train)  | [Bactrian-fi](https://huggingface.co/haonan-li/bactrian-fi-7b-lora) |  |
| 12 | French          | [fr_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/fr/train)  | [Bactrian-fr](https://huggingface.co/haonan-li/bactrian-fr-7b-lora) |  |
| 13 | Galician        | [gl_ES](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/gl/train)  | [Bactrian-gl](https://huggingface.co/haonan-li/bactrian-gl-7b-lora) |  |
| 14 | Gujarati        | [gu_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/gu/train)  | [Bactrian-gu](https://huggingface.co/haonan-li/bactrian-gu-7b-lora) |  |
| 15 | Hebrew          | [he_IL](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/he/train)  | [Bactrian-he](https://huggingface.co/haonan-li/bactrian-he-7b-lora) |  |
| 16 | Hindi           | [hi_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/hi/train)  | [Bactrian-hi](https://huggingface.co/haonan-li/bactrian-hi-7b-lora) |  |
| 17 | Croatian        | [hr_HR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/hr/train)  | [Bactrian-hr](https://huggingface.co/haonan-li/bactrian-hr-7b-lora) |  |
| 18 | Indonesian      | [id_ID](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/id/train)  | [Bactrian-id](https://huggingface.co/haonan-li/bactrian-id-7b-lora) |  |
| 19 | Italian         | [it_IT](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/it/train)  | [Bactrian-it](https://huggingface.co/haonan-li/bactrian-it-7b-lora) |  |
| 20 | Japanese        | [ja_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ja/train)  | [Bactrian-ja](https://huggingface.co/haonan-li/bactrian-ja-7b-lora) |  |
| 21 | Georgian        | [ka_GE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ka/train)  | [Bactrian-ka](https://huggingface.co/haonan-li/bactrian-ka-7b-lora) |  |
| 22 | Kazakh          | [kk_KZ](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/kk/train)  | [Bactrian-kk](https://huggingface.co/haonan-li/bactrian-kk-7b-lora) |  |
| 23 | Khmer           | [km_KH](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/km/train)  | [Bactrian-km](https://huggingface.co/haonan-li/bactrian-km-7b-lora) |  |
| 24 | Korean          | [ko_KR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ko/train)  | [Bactrian-ko](https://huggingface.co/haonan-li/bactrian-ko-7b-lora) |  |
| 25 | Lithuanian      | [lt_LT](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/lt/train)  | [Bactrian-lt](https://huggingface.co/haonan-li/bactrian-lt-7b-lora) |  |
| 26 | Latvian         | [lv_LV](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/lv/train)  | [Bactrian-lv](https://huggingface.co/haonan-li/bactrian-lv-7b-lora) |  |
| 27 | Macedonian      | [mk_MK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mk/train)  | [Bactrian-mk](https://huggingface.co/haonan-li/bactrian-mk-7b-lora) |  |
| 28 | Malayalam       | [ml_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ml/train)  | [Bactrian-ml](https://huggingface.co/haonan-li/bactrian-ml-7b-lora) |  |
| 29 | Mongolian       | [mn_MN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mn/train)  | [Bactrian-mn](https://huggingface.co/haonan-li/bactrian-mn-7b-lora) |  |
| 30 | Marathi         | [mr_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/mr/train)  | [Bactrian-mr](https://huggingface.co/haonan-li/bactrian-mr-7b-lora) |  |
| 31 | Burmese         | [my_MM](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/my/train)  | [Bactrian-my](https://huggingface.co/haonan-li/bactrian-my-7b-lora) |  |
| 32 | Nepali          | [ne_NP](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ne/train)  | [Bactrian-ne](https://huggingface.co/haonan-li/bactrian-ne-7b-lora) |  |
| 33 | Dutch           | [nl_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/nl/train)  | [Bactrian-nl](https://huggingface.co/haonan-li/bactrian-nl-7b-lora) |  |
| 34 | Polish          | [pl_PL](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/pl/train)  | [Bactrian-pl](https://huggingface.co/haonan-li/bactrian-pl-7b-lora) |  |
| 35 | Pashto          | [ps_AF](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ps/train)  | [Bactrian-ps](https://huggingface.co/haonan-li/bactrian-ps-7b-lora) |  |
| 36 | Portuguese      | [pt_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/pt/train)  | [Bactrian-pt](https://huggingface.co/haonan-li/bactrian-pt-7b-lora) |  |
| 37 | Romanian        | [ro_RO](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ro/train)  | [Bactrian-ro](https://huggingface.co/haonan-li/bactrian-ro-7b-lora) |  |
| 38 | Russian         | [ru_RU](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ru/train)  | [Bactrian-ru](https://huggingface.co/haonan-li/bactrian-ru-7b-lora) |  |
| 39 | Sinhala         | [si_LK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/si/train)  | [Bactrian-si](https://huggingface.co/haonan-li/bactrian-si-7b-lora) |  |
| 40 | Slovene         | [sl_SI](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sl/train)  | [Bactrian-sl](https://huggingface.co/haonan-li/bactrian-sl-7b-lora) |  |
| 41 | Swedish         | [sv_SE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sv/train)  | [Bactrian-sv](https://huggingface.co/haonan-li/bactrian-sv-7b-lora) |  |
| 42 | Swahili         | [sw_KE](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/sw/train)  | [Bactrian-sw](https://huggingface.co/haonan-li/bactrian-sw-7b-lora) |  |
| 43 | Tamil           | [ta_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ta/train)  | [Bactrian-ta](https://huggingface.co/haonan-li/bactrian-ta-7b-lora) |  |
| 44 | Telugu          | [te_IN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/te/train)  | [Bactrian-te](https://huggingface.co/haonan-li/bactrian-te-7b-lora) |  |
| 45 | Thai            | [th_TH](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/th/train)  | [Bactrian-th](https://huggingface.co/haonan-li/bactrian-th-7b-lora) |  |
| 46 | Tagalog         | [tl_XX](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/tl/train)  | [Bactrian-tl](https://huggingface.co/haonan-li/bactrian-tl-7b-lora) |  |
| 47 | Turkish         | [tr_TR](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/tr/train)  | [Bactrian-tr](https://huggingface.co/haonan-li/bactrian-tr-7b-lora) |  |
| 48 | Ukrainian       | [uk_UA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/uk/train)  | [Bactrian-uk](https://huggingface.co/haonan-li/bactrian-uk-7b-lora) |  |
| 49 | Urdu            | [ur_PK](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/ur/train)  | [Bactrian-ur](https://huggingface.co/haonan-li/bactrian-ur-7b-lora) |  |
| 50 | Vietnamese      | [vi_VN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/vi/train)  | [Bactrian-vi](https://huggingface.co/haonan-li/bactrian-vi-7b-lora) |  |
| 51 | Xhosa           | [xh_ZA](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/xh/train)  | [Bactrian-xh](https://huggingface.co/haonan-li/bactrian-xh-7b-lora) |  |
| 52 | Chinese         | [zh_CN](https://huggingface.co/datasets/MBZUAI/Bactrian-X/viewer/zh/train)  | [Bactrian-zh](https://huggingface.co/haonan-li/bactrian-zh-7b-lora) |  |

## Model Training and Inference

The code base for training and inference is adapted from [Alpaca-LoRA](https://github.com/tloen/alpaca-lora).

### Local Setting

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. If `bitsandbytes` doesn't work, [install it from source.](https://github.com/TimDettmers/bitsandbytes/blob/main/compile_from_source.md) Windows users can follow [these instructions](https://github.com/tloen/alpaca-lora/issues/17).

### Training

Models are trained with the following hyperparameters:

| Hyper-parameter | Bactrian-{lang} | Bactrian-X |
| --------------- | --------------- | ---------- |
| batch_size      | 128             | 256        |
| num_epochs      | 10              | 10         |
| learning_rate   | 3e-4            | 3e-4       |
| cutoff_len      | 512             | 512        |
| lora_r          | 16              | 64         |
| lora_alpha      | 16              | 16         |

Below is a command that trains a LLaMA-7B adapter with our datasets in specific language(s). Replace `<lang_iso>` with a list of (one or more) language iso code separated by comma `,` (e.g., `en,zh` for `English` and `Chinese`), and `<your_output_dir>` with where you want to store your outputs.

```bash
python finetune.py \
--base_model 'decapoda-research/llama-7b-hf' \
    --data_path 'MBZUAI/Bactrian-X' \
    --lang <lang_iso> \
    --output_dir <your_output_dir> \
    --batch_size 128 \
    --micro_batch_size 32 \
    --num_epochs 10 \
    --learning_rate 3e-4 \
    --cutoff_len 512 \
    --val_set_size 2000 \
    --lora_r 16 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q_proj,k_proj,v_proj,o_proj' \
    --train_on_inputs \
    --group_by_length
```


### Inference

This is an example code that loads both foundation model and Bactrian LoRA weights from the Hugging Face model hub, and runs a Gradio interface for inference on a specified input. 
```bash
python generate.py \
    --load_8bit \
    --base_model 'decapoda-research/llama-7b-hf' \
    --lora_weights 'MBZUAI/bactrian-x-7b-lora' \
    --share_gradio 
```

### Checkpoint export 

To merge the LoRA weights back into the base model for export to Hugging Face format and to PyTorch `state_dicts`, go to [Alpaca-LoRA](https://github.com/tloen/alpaca-lora).
They should help users who want to run inference in projects like [llama.cpp](https://github.com/ggerganov/llama.cpp) or [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp).


## Citation

Please cite the repo if you use the data, model or code in this repo. Our paper will be released very soon.

```
@misc{bactrian,
  author = {Haonan Li and Fajri Koto and Timothy Baldwin},
  title = {Bactrian-X: A Multilingual Replicable Instruction-Following Model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/MBZUAI-nlp/Bactrian-X}},
}
```

Naturally, you should also cite the original [LLaMA paper](https://arxiv.org/abs/2302.13971), the [Self-Instruct paper](https://arxiv.org/abs/2212.10560), and the [Stanford Alpaca repo](https://github.com/tatsu-lab/stanford_alpaca).
