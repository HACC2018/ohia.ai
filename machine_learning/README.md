
## Table of contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Preprocessing](#requirements)
* [Training](#requirements)
   * [Datasets](#datasets)
   * [Models](#models)
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

If these requirements make it impossible for you to use our code, please open an issue and we will try to accommodate you.


## Preprocessing

Run `preprocess.py` to 


## Training


### Datasets
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

See `data_collection` for more details.


### Models

Our team utilizes multi-stage transfer-learning to mitigate the need for extremely large datasets.

* First, we obtain [base models](https://keras.io/applications/) which are pretrained on ImageNet.  These pretrained models have learned salient features of real-world images. By using these base models as a starting point, we can avoid having to train on 
* Next, we retrain the base models on PlantNet.  This allows our neural networks to learn plant specific features in the images.   
* Finally, we fine-tune our models on the scraped dataset which consists of images of plants found in Hawaii.

### Results
|            model | filtered |  augmentation | top 1 accuracy | top 3 accuracy | top 5 accuracy |
| ---------------- | -------- | ------------- | -------------- | -------------- | -------------- |
| mobilenetv1-1.00 |       No |            No |         0.6450 |         0.8559 |         0.9219 |
| mobilenetv2-1.00 |       No |            No |         0.5521 |         0.7786 |         0.8698 |
| mobilenetv2-1.30 |       No |            No |         0.5842 |         0.8290 |         0.8993 |
| mobilenetv2-1.40 |       No |            No |         0.6068 |         0.8490 |         0.9149 |
|     nasnetmobile |       No |            No |         0.5590 |         0.8056 |         0.8854 |


## References
* [1] [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf)


