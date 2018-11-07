## Table of contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Preprocessing](#preprocessing)
* [Datasets](#datasets)
* [Training](#training)
   * [Data Augmentation](#data-augmentation)
   * [Model Architectures](#model-architectures)
   * [Transfer Learning](#transfer-learning)
* [Results](#results)

## Introduction

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiian Islands.


## Requirements

To run our script you will need:

* Python version >=3.6
* [NumPy](http://www.numpy.org/) - General purpose numerical computing
* [SciPy](https://www.scipy.org/) - Scientific computing utilities
* [Keras](https://keras.io/) - High level API for neural network design and training
* [pandas](https://pandas.pydata.org/) - Data frames for python
* [PIL](https://pillow.readthedocs.io/en/5.3.x/) - Image processing tools
* [Click](https://click.palletsprojects.com/en/7.x/) - CLI tools

If these requirements make it impossible for you to use our code, please open an issue and we will try to accommodate you.


## Preprocessing

Run `preprocess.py` to resize and possibly crop images.  

```
>>> python preprocess.py --help

Usage: preprocess.py [OPTIONS]

Options:
  --input_dir TEXT     Input directory of images.  [required]
  --output_dir TEXT    Output directory of images.  [required]
  --file_path TEXT     Absolute path to data directories.
  --min_count INTEGER  Minimum numbers of images needed to create a class.
  --n_thread INTEGER   Number of threads to use.
  --crop TEXT          Either: "center", "triangular" or "uniform".
  --help               Show this message and exit.
```

In our experiments we resize the smaller dimension of image to 224 pixels.  This size produces a good tradeoff between having high resolution images and high accuracy and being able to process the images quickly.  


## Datasets
Deep learning is notorious for needing large amounts of data to perform well [1](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf).  Our models are trained on a number of different datasets: custom scraped data, [PlantNet](https://www.imageclef.org/lifeclef/2017/plant), [ImageNet](http://www.image-net.org/).  See our `data_collection/README.md` for more details.


## Training
In machine learning, "training" refers to the process of learning from data.  

```
python train.py --help
Usage: train.py [OPTIONS]

Options:
  --model_name TEXT        Name of neural network architecture: "mobilenetv1", "mobilenetv2", "nasnetmobile" [required]
  --training_type INTEGER  Integer encoding: 0=fine-tune, 1=pretrain, 2=load pretrained then fine-tune.
  --seed INTEGER           Random seed.
  --batch_size INTEGER     Number of observations needed before updating weights.
  --augmentation TEXT      Boolean flag.  If true then perform data augmentation.
  --gpu INTEGER            Which gpu to use.
  --n_thread INTEGER       Number of threads to use.
  --save_model TEXT        Boolean flag.  If true then save the model in a tfjs format.
  --help                   Show this message and exit.
```

Our training was performed on two NVIDIA GeForce GTX 1080 Ti GPUs.  You can specify which gpu to use using the `--gpu` parameter.  Because of the large size of the data, we created a generator to stream data in batches onto the GPU in parallel.  The `--n_thread` determines the number of CPU cores to use in the generator.  The `--batch_size` parameter determines the size of the batch, we used 32.  


### Data Augmentation

Data augmentation is a technique used to create more realistic data for our models to train on.  Data augmentation is a common technique used to increase the performance of neural neworks. Our team leverages the following data augmentation techniques:

* Random crops (the center of the crop has a triangular distribution)
* Horizontal flips
* Random brightness transformations


The `--augmentation` parameter is a binary flag that turns on/off data augmentation.

### Model Architectures

We used/compared the following state-of-the-art lightweight neural network architectures:

Architecture | Research Paper
-- | -- 
[MobileNet](https://keras.io/applications/#mobilenet) | [MobileNet: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/pdf/1704.04861.pdf)
[MobileNetV2](https://keras.io/applications/#mobilenetv2) | [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
[NASNetMobile](https://keras.io/applications/#nasnet) | [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012)

The `--model_name` parameter specifies which architecture to use.  Use the `--save_model` parameter to save the model in a format that can be used by TensorflowJS.

### Transfer Learning
Transfer learning allowed our team to reuse features learned by neural networks.  Our team utilizes multi-stage transfer learning to mitigate the need for extremely large datasets.

1. Obtain base models which are pretrained on ImageNet.  These pretrained models have learned salient features of real-world images. By using these base models as a starting point, we can avoid having to train on 
2. Retrain the base models on PlantNet.  This allows our neural networks to learn plant specific features in the images.   
3. Fine-tune our models on the scraped dataset which consists of images of plants found in Hawaii.

The `--training_type` parameter defines the stage of training. 

## Results

We validate using a 10% validation set.  The `--seed` parameter specifies the random seed used in the training/validation split.  The metrics that we were concerned with were the

* Top 1 Accuracy - The fraction of time the correct answer equals the top prediction.
* Top 3 Accuracy - The fraction of time the correct answer was in the top 3 predictions.
* Top 5 Accuracy - The fraction of time the correct answer was in the top 5 predictions.


| Architecture | Pretraining | Augmentation | Top 1 Accuracy | Top 3 Accuracy | Top 5 Accuracy |
| ------------ | ----------- | ------------ | -------------- | -------------- | -------------- |
|  mobilenetv1 |    ImageNet |           No |         0.5436 |         0.7618 |         0.8396 |
|  mobilenetv1 |    ImageNet |          yes |         0.7394 |         0.8856 |         0.9257 |
|  mobilenetv1 |    PlantNet |          Yes |         0.7376 |         0.8874 |         0.9251 |
|  mobilenetv2 |    PlantNet |          Yes |         0.7453 |         0.8850 |         0.9240 |
| nasnetmobile |    PlantNet |          Yes |         0.7547 |         0.8774 |         0.9204 |

The best model consisted of a MobileNetV1 architecture, pretraining on PlantNet, and data augmentation.

 