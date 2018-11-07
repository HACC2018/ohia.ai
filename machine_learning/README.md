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

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiiain Islands.


## Requirements

To run our script you will need:

* Python version >=3.6
* [NumPy](http://www.numpy.org/) - General purpose numerical computing
* [SciPy](https://www.scipy.org/) - Scientific computing utilities
* [Keras](https://keras.io/) - High level API for neural network design and training
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

In our experiements we resize the smaller dimension of image to 224 pixels.  This size produces a good tradeoff between having high resolution images and high accuracy and being able to process the images quickly.  


## Datasets
Deep learning is notorious for needing large amounts of data to perform well [1].  Our models are trained on a number of different datasets:

| Source | Preprocessing | Number of Images | Number of Classes (Plants) |
| -------| ------------- |----------------- | -------------------------- |
| Scraped | None | 21,070 | 42 |
| Scraped | Removed non-plant images | 17,263 | 42 |
| [PlantNet](https://www.imageclef.org/lifeclef/2017/plant) | None | 264,795 | 9,968 |
| [PlantNet](https://www.imageclef.org/lifeclef/2017/plant) | Removed species with fewer than 100 images | 81,834 | 436 |
| [ImageNet](http://www.image-net.org/) | None | 1,281,167 | 1000 |


Our team scraped datas from the following sites:
* [Starr Environmental](http://starrenvironmental.com/images/)
* [Wild Life of Hawaii](https://wildlifeofhawaii.com/flowers/category/native-status/native-plants/)
* [Hawaiian Ethnobotony Online Database](http://data.bishopmuseum.org/ethnobotanydb/ethnobotany.php?b=list&amp;o=2)
* [Canoe Plants of Ancient Hawaii](http://www.canoeplants.com/contents.html)
* [Native Plants Hawaii](http://nativeplants.hawaii.edu/)

Many of the scraped images are of non-plants.  We filtered out the non-plant images before training our models.  See our data_collection dir for more details.


## Training
In machine learning, "training" referes to the process of learning from data.  

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


### Data Augmentation

Data augmentation is a technique used to create more realistic data for our models to train on.  Data augmentation is a common technique used to increase the performance of neural neworks [2]. Our team leverages the following data augmentation techniques:

* Random crops (the center of the crop has a triangular distribution)
* Horizontal flips
* Random brightness transformations


The `--augmentation` parameter is a binary flag that turns on/off data augmentation.

### Model Architectures

We used/compared the following state-of-the-art lightweight neural network architechures:

Architecture | Research Paper
-- | -- 
[MobileNet](https://keras.io/applications/#mobilenet) | [MobileNet: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/pdf/1704.04861.pdf)
[MobileNetV2](https://keras.io/applications/#mobilenetv2) | [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
[NASNetMobile](https://keras.io/applications/#nasnet) | [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012)

The `--model_name` parameter specifies which architechture to use.

### Transfer Learning
Transfer learning [3] allowed our team to reuse features learned by neural networks.  Our team utilizes multi-stage transfer learning to mitigate the need for extremely large datasets.

1. Obtain base models which are pretrained on ImageNet.  These pretrained models have learned salient features of real-world images. By using these base models as a starting point, we can avoid having to train on 
2. Retrain the base models on PlantNet.  This allows our neural networks to learn plant specific features in the images.   
3. Fine-tune our models on the scraped dataset which consists of images of plants found in Hawaii.

The `--training_type` parameter defines the stage of training. 

## Results

We validate using a 10% validation set.  The metrics that we were concerened with were the

* Top 1 Accuracy - the fraction of time the correct answer equals the top prediction
* Top 3 Accuracy - the fraction of time the correct answer was in the top 3 predictions
* Top 5 Accuracy - the fraction of time the correct answer was in the top 5 predictions


|   Architechture |  Pretraining |  Augmentation | Top 1 Accuracy | Top 3 Accuracy | Top 5 Accuracy |
| --------------- | ------------ | ------------- | -------------- | -------------- | -------------- |
|     mobilenetv1 |     ImageNet |            No |         0.5521 |         0.7786 |         0.8698 |
|     mobilenetv1 |     ImageNet |           yes |         0.5842 |         0.8290 |         0.8993 |
| **mobilenetv1** | **PlantNet** |       **Yes** |     **0.6450** |     **0.8559** |     **0.9219** |
|     mobilenetv2 |     PlantNet |           Yes |         0.6068 |         0.8490 |         0.9149 |
|    nasnetmobile |     PlantNet |           Yes |         0.5590 |         0.8056 |         0.8854 |

The best model consisted of a MobileNetV1 architechture, pretraining on PlantNet, and data augmentation.


## References
* [1] [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf)
* [2] [Data Augmentation](https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced)
* [3] [Transfer Learning](https://en.wikipedia.org/wiki/Transfer_learning)


