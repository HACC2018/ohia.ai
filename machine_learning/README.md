
## Table of contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Preprocessing](#requirements)
* [Training](#requirements)
   * [Datasets](#datasets)
   * [Models](#models)
* [Results](#results)


## Introduction

Behind the scenes, ohia.ai is powered by machine learning and AI.  Out team utilizes modern deep learning frameworks and large open source datasets to achieve high accuracy classification on a wide range of flora found throughout the Hawaiiain Islands.


## Requirements

To run our script you will need:

* Python version >=3.6
* [NumPy](http://www.numpy.org/) - General purpose numerical computing
* [SciPy](https://www.scipy.org/) - Scientific computing utilities
* [Keras](https://keras.io/) - High level API for neural network design and training
* [PIL](https://pillow.readthedocs.io/en/5.3.x/) - Image processing tools

If these requirements make it impossible for you to use our code, please open an issue and we will try to accommodate you.


## Preprocessing


## Training


### Datasets
Deep learning is notorious for needing large amounts of data to perform well [1]



| Source            | Number of Images | Number of Classes (Plants) |
| ----------------- | ---------------- | -------------------------- |
| Scraped           | 21,070           | 42                         |
| Filtered Scraped  | 17,263           | 42                         |
| PlantNet          | 264,795          | 9,968                      |
| Filtered PlantNet | 81,834           | 436                        |
| ImageNet          | 1,281,167        | 1000                       |


Run `preprocess.py` to 


### Models
- Recent state-of-the-art [English word vectors](https://fasttext.cc/docs/en/english-vectors.html).
- Word vectors for [157 languages trained on Wikipedia and Crawl](https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md).
- Models for [language identification](https://fasttext.cc/docs/en/language-identification.html#content) and [various supervised tasks](https://fasttext.cc/docs/en/supervised-models.html#content).


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


