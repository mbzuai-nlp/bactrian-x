lang='af,ar,az,bn,cs,de,en,es,et,fa,fi,fr,gl,gu,he,hi,hr,id,it,ja,ka,kk,km,ko,lt,lv,mk,ml,mn,mr,my,ne,nl,pl,ps,pt,ro,ru,si,sl,sv,sw,ta,te,th,tl,tr,uk,ur,vi,xh,zh'
model_size='xl'
WORLD_SIZE=4
CUDA_VISIBLE_DEVICES=0,1,2,3

torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
--model_name_or_path google/mt5-${model_size} \
--lang ${lang} \
--output_dir output/mt5-${model_size}-X-lora \
--overwrite_output_dir \
--template_dir ./templates \
--learning_rate 3e-4 \
--load_in_8bit \
--per_device_train_batch_size 8 \
--per_device_eval_batch_size 4 \
--gradient_accumulation_steps 4 \
--num_train_epochs 4 \
--source_max_length 256 \
--model_max_length 768 \
--val_set_size 5000 \
--save_steps 2000 \
--eval_steps 2000 \
--logging_steps 100 \
--preprocessing_num_workers 4 \
--dataloader_num_workers 4 \
--lora_r 64 \
--lora_alpha 16 \
--lora_dropout 0.05 \
--lora_target_modules 'q,v' \
--ddp_find_unused_parameters False \
--save_total_limit 10 \
--group_by_length \
--report_to wandb \
--wandb_project bactrian-X \
--run_name mt5-${model_size}-X
