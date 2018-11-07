# preprocesssing
python preprocess.py \
  --input_dir raw_images/scraped \
  --output_dir preprocessed_images/scraped \
  --n_thread 20

python preprocess.py \
  --input_dir scraped_filtered \
  --output_dir preprocessed_images/scraped_filtered \
  --n_thread 20

python preprocess.py \
  --input_dir /media/matt/storage0/plant_images/image_clef_2017/train \
  --output_dir preprocessed_images/plantnet \
  --n_thread 20


 # Augmentation
python train.py \
  --model_name mobilenetv1 \
  --training_type 0 \
  --n_thread 20 \
  --save_model True \
  --gpu 0

python train.py \
  --model_name mobilenetv1 \
  --training_type 0 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 1


python train.py \
  --model_name mobilenetv2 \
  --training_type 0 \
  --n_thread 20 \
  --save_model True \
  --gpu 0

python train.py \
  --model_name mobilenetv2 \
  --training_type 0 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 1


python train.py \
  --model_name nasnetmobile \
  --training_type 0 \
  --n_thread 20 \
  --save_model True \
  --gpu 0

python train.py \
  --model_name nasnetmobile \
  --training_type 0 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 1


# Pretraining
python train.py \
  --model_name mobilenetv1 \
  --training_type 1 \
  --n_thread 20 \
  --save_model True \
  --gpu 0

python train.py \
  --model_name mobilenetv2 \
  --training_type 1 \
  --n_thread 20 \
  --save_model True \
  --gpu 1

python train.py \
  --model_name nasnetmobile \
  --training_type 1 \
  --n_thread 20 \
  --save_model True \
  --gpu 1


# Finetune
python train.py \
  --model_name mobilenetv1 \
  --training_type 2 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 0

python train.py \
  --model_name mobilenetv2 \
  --training_type 2 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 1

python train.py \
  --model_name nasnetmobile \
  --training_type 2 \
  --augmentation True \
  --n_thread 20 \
  --save_model True \
  --gpu 1
