## Table of contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Scraping](#scraping)
* [Datasets](#datasets)
* [References](#references)


## Introduction

Machine learning is the processs of learning from data, thus data collection is an integral part of our application.  Without data we would not be able to do machine learning.


## Requirements

To run our script you will need:

* R version >= 3.5.1
* [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) - High performance data frames
* [rvest](https://github.com/hadley/rvest) - Web scraping utilities
* [parallel](https://stat.ethz.ch/R-manual/R-devel/library/parallel/doc/parallel.pdf) - Parallel processing library
* [xml2](https://github.com/r-lib/xml2) - XML tools
* [Rselenium](https://ropensci.org/tutorials/rselenium_tutorial/) - Tools for Selenium server

If these requirements make it impossible for you to use our code, please open an issue and we will try to accommodate you.


## Scraping

To develop a neural network capable of classifying plants in images, we collected images from multiple sources including but not limited to Wikicommons, starrenvironmental.com, Flickr, Instagram, and Google Images filtered by license. Automated collection was separated by plant genus, as it was mentioned some professionals may have difficulty in identifying species under non-flowering conditions. In addition to native plants, we collected images for common plants in the islands for general use. We used Rvest, Selenium, and a multitude of python libraries in an AWS EC2 instance to collect images. Resulting image dataset was noisy (including non-plant images). A relatively clean final dataset was ensured by manual curation by Ohia.ai members.


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

Many of the scraped images are of non-plants.  We filtered out the non-plant images before training our models.  



## References
* [1] [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf)
* [2] [Data Augmentation](https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced)
* [3] [Transfer Learning](https://en.wikipedia.org/wiki/Transfer_learning)


