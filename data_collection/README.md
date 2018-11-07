## Table of contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Scraping](#scraping)
* [Datasets](#datasets)
   * [ImageNet](#imagenet)
   * [PlantNet](#plantnet)

## Introduction

Machine learning involves learning from data, thus data collection is an integral part of our application.  Here is summary of the data that our team collected.

| Source | Preprocessing | Number of Images | Number of Classes (Plants) |
| -------| ------------- |----------------- | -------------------------- |
| Scraped | None | 21,070 | 42 |
| Scraped | Removed non-plant images | 17,263 | 42 |
| PlantNet | None | 264,795 | 9,968 |
| PlantNet | Removed species with fewer than 100 images | 81,834 | 436 |
| ImageNet | None | 1,281,167 | 1000 |

## Requirements

To run our R scripts you will need `R version >= 3.5.1` and the following packages:
* [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) - High performance data frames
* [Tidyverse](https://www.tidyverse.org/l) - A collection of useful R packages
* [rvest](https://github.com/hadley/rvest) - Web scraping utilities
* [parallel](https://stat.ethz.ch/R-manual/R-devel/library/parallel/doc/parallel.pdf) - Parallel processing library
* [xml2](https://github.com/r-lib/xml2) - XML tools
* [Rselenium](https://ropensci.org/tutorials/rselenium_tutorial/) - R language bindings for Selenium WebDriver

To run our python scripts you will need `python version >= 3.6` and the following packages:
* [pandas](https://pandas.pydata.org/) - Open source high-performance easy-to-use data structures and data analysis tools
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Framework for web scraping and parsing HTML and XML files
* [selenium](https://pypi.org/project/selenium/) - Python language bindings for Selenium WebDriver
* [json](https://docs.python.org/3/library/json.html) - Utilities for working with JSON files

If these requirements make it impossible for you to use our code, please open an issue and we will try to accommodate you.


## Scraping

Our team scraped data from multiple sources including but not limited to : [Starr Environmental](http://starrenvironmental.com/images/), [Wild Life of Hawaii](https://wildlifeofhawaii.com/flowers/category/native-status/native-plants/), [Hawaiian Ethnobotony Online Database](http://data.bishopmuseum.org/ethnobotanydb/ethnobotany.php?b=list&amp;o=2), [Google Images](https://www.google.com/imghp?hl=en&tab=wi&authuser=0), [Instagram](https://www.instagram.com/?hl=en), [Flickr](https://www.flickr.com/), [Native Plants Hawaii](http://nativeplants.hawaii.edu/), [Wikicommons](https://commons.wikimedia.org/wiki/Main_Page), , [Canoe Plants of Ancient Hawaii](http://www.canoeplants.com/contents.html).

The data collected was filtered by license.  Our automated collection was separated by plant genus, as it was mentioned some professionals may have difficulty in identifying species under non-flowering conditions. In addition to native plants, we collected images for common plants in the islands for general use. We ran our scraping scripts locally and on an AWS EC2 instance.  The resulting image dataset was noisy (including non-plant images). A relatively clean final dataset was ensured by manual duration by ohia.ai members.


## Datasets

In addition to manually obtaining collecting data, our team utilized large open source image repositories. Our team made use of the [ImageNet](http://www.image-net.org/) repository and the 2017 CLEF [PlantNet](https://www.imageclef.org/lifeclef/2017/plant) dataset.

### ImageNet

ImageNet is an ongoing research effort to provide researchers around the world an easily accessible image database.  It is used as a benchmark on many computer vision tasks. ImageNet however does not have any categories for plants but we were still able to utilize this dataset in the form of transfer learning.  See our `machine_learning/README.md` for more details.

### PlantNet

PlantNet is a large open source data consisting of only plants.  The raw data has over 250,000 images of nearly 10,000 species of plant.  Predicting all 10,000 species would be a very difficult task especially since more than 95% of the species had fewer than 100 images.  Our team filtered out the species with fewer than 100 images and used the resulting dataset to train specialized models.  These specialized models outperformed models that did not take advantage of these valuable source of data.  See our `machine_learning/README.md` for more details.


