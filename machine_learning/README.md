
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

Behind the scenes, ohia.ai is powered by machine learning and AI.  Out team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiiain Islands.


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
| PlantNet | None | 264,795 | 9,968 |
| PlantNet | Removed species with fewer than 100 images | 81,834 | 436 |
| ImageNet | None | 1,281,167 | 1000 |


The `Scraped` dataset consists of images from:
* [Starr Environmental](http://starrenvironmental.com/images/)
* [Wild Life of Hawaii](https://wildlifeofhawaii.com/flowers/category/native-status/native-plants/)
* [Hawaiian Ethnobotony Online Database](http://data.bishopmuseum.org/ethnobotanydb/ethnobotany.php?b=list&amp;o=2)
* [Canoe Plants of Ancient Hawaii](http://www.canoeplants.com/contents.html)
* [Native Plants Hawaii](http://nativeplants.hawaii.edu/)

Many of the scraped images are of non-plants.  We filtered out the non-plant images before training our models.  

See `data_collection` for more details.


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

Data augmentation is a technique used to create more realistic data for our models to train on.  Our team leverages the following data augmentation techniques:

* Random crops (the center of the crop has a triangular distribution)
* Horizontal flips
* Random brightness transformations

### Model Architechures

### Transfer Learning
Our team utilizes multi-stage transfer learning to mitigate the need for extremely large datasets.

* First, we obtain [base models](https://keras.io/applications/) which are pretrained on ImageNet.  These pretrained models have learned salient features of real-world images. By using these base models as a starting point, we can avoid having to train on 
* Next, we retrain the base models on PlantNet.  This allows our neural networks to learn plant specific features in the images.   
* Finally, we fine-tune our models on the scraped dataset which consists of images of plants found in Hawaii.


## Results
|            model | filtered |  augmentation | top 1 accuracy | top 3 accuracy | top 5 accuracy |
| ---------------- | -------- | ------------- | -------------- | -------------- | -------------- |
| mobilenetv1-1.00 |       No |            No |         0.6450 |         0.8559 |         0.9219 |
| mobilenetv2-1.00 |       No |            No |         0.5521 |         0.7786 |         0.8698 |
| mobilenetv2-1.30 |       No |            No |         0.5842 |         0.8290 |         0.8993 |
| mobilenetv2-1.40 |       No |            No |         0.6068 |         0.8490 |         0.9149 |
|     nasnetmobile |       No |            No |         0.5590 |         0.8056 |         0.8854 |


## References
* [1] [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf)
* [2] [Transfer Learning](https://en.wikipedia.org/wiki/Transfer_learning)
* [3] [Data Augmentation](https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced)

