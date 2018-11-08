# ohia.ai

An open Hawaiian indigenous plant identification and aggregation application. Developed for the 2018 Hawaii Annual Code Challenge.

## Table of Contents

* [Overview](#overview)
* [Quick Start Application](#quick-start-application)
* [Complete Application Setup](#complete-application-setup)
* [Data Collection](#data-collection)
* [Machine Learning](#machine-learning)
* [Results](#results)
* [Usage](#usage)

## Overview

To get started, first read the introductory text under **Quick Start Application**. Or read the **Data Collection**, **Machine Learning**, and **Results** sections of this README. 

When ready for more information about each step of the process, visit any of the following:
- [API Server](https://github.com/HACC2018/ohia.ai/tree/master/server)
- [App Client](https://github.com/HACC2018/ohia.ai/tree/master/client)
- [Data Collection](https://github.com/HACC2018/ohia.ai/tree/master/data_collection)
- [Machine Learning](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning)

## Quick Start Application

Our app was built for the iPhone 6 running on iOS version 12. However, deploying the app to an iPhone device is a long process, especially if your Mac is not up-to-date with the latest OS or Xcode version. Therefore, we recommend these quick start steps for getting up-and-running quickly on the browser. Note, however, that the main feature of the app, plant identification, will not work because the native iOS camera cannot run on the browser.

If you would rather follow the complete instructions and deploy to an iOS device, follow the steps under [Complete Application Setup](#complete-application-setup).

### Getting Started
1. Clone this repository by running the following command in a terminal: `git clone git@github.com:HACC2018/ohia.ai.git`.
1. Change into the ohia.ai project directory: `cd ohia.ai`.
1. When running anything related to the client or server, we require Python 2.7 to be installed, since that is the version that the [tfjs-node](https://github.com/tensorflow/tfjs-node) package supports. Switch your terminal to use Python 2.7 (more information [here](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-python-required)).
1. Switch your terminal to use Node 10.12.0 (more information [here](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-nodejs-required)).

### Install server dependencies and run the server
1. From the project root directory, run `npm install`. Among other items, you should see "Downloading libtensorflow" and "Building TensorFlow Node.js bindings" run without error in your output.
1. Create a `.env` file in the project root by copying the template in `.env.sample`.
1. Source your environment by running: `source .env`.
1. You should now see these variables in your environment by running `env`.
1. Run the server: `npm run dev-server`. You should see the following output:
    ```
    ▶ npm run dev-server

    > ohia.ai@0.0.1 dev-server /path/to/ohia.ai
    > nodemon server/index.js

    [nodemon] 1.18.4
    [nodemon] to restart at any time, enter `rs`
    [nodemon] watching: *.*
    [nodemon] starting `node server/index.js`
    2018-11-07 07:25:31.386112: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.2 AVX AVX2 FMA
    Server for ohia.ai listening on port 3000
    ```

### Install Vue.js and Quasar and run the client in a browser
1. Open another terminal window and switch to Python 2.7 and Node 10.12.0.
1. Source the environment: `source .env`.
1. Install Vue CLI: `npm install -g @vue/cli`.
1. Install Vue CLI addon: `npm install -g @vue/cli-init`.
1. Install Quasar CLI: `npm install -g quasar-cli`.
1. From the project root directory, install client dependencies: `npm run install:client`.
1. Run `npm run dev` to view the app in a browser. You should see the following output:
    ```
    ▶ npm run install:client

    > ohia.ai@0.0.1 install:client ~/ohia.ai
    > cd client && npm install


    > fsevents@1.2.4 install ~/ohia.ai/client/node_modules/fsevents
    > node install

    [fsevents] Success: "~/ohia.ai/client/node_modules/fsevents/lib/binding/Release/node-v64-darwin-x64/fse.node" already installed
    Pass --update-binary to reinstall or --build-from-source to recompile
    added 1333 packages from 612 contributors and audited 16152 packages in 23.649s
    found 0 vulnerabilities

    (python2)
    ```
1. Visit http://localhost:8080 to view the app.
1. The app is [best viewed by enabling the Chrome device toolbar and setting the device to iPhone 6/7/8](https://s3-us-west-2.amazonaws.com/ohia.ai/chrome_device_toolbar.png).

## Complete Application Setup

### Getting Started
1. Clone this repository by running the following command in a terminal: `git clone git@github.com:HACC2018/ohia.ai.git`.
1. Change into the ohia.ai project directory: `cd ohia.ai`.
1. When running anything related to the client or server, we require Python 2.7 to be installed, since that is the version that the [tfjs-node](https://github.com/tensorflow/tfjs-node) package supports. Switch your terminal to use Python 2.7 (more information [here](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-python-required)).
1. Switch your terminal to use Node 10.12.0 (more information [here](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-nodejs-required)).

### Installation and Execution
1. Follow the instructions on the [API Server](https://github.com/HACC2018/ohia.ai/tree/master/server) README.
1. Follow the instructions on the [App Client](https://github.com/HACC2018/ohia.ai/tree/master/client) README.

## Data Collection

Machine learning involves learning from data, thus data collection is an integral part of our application.  For more details see [ohia.ai/data_collection](https://github.com/HACC2018/ohia.ai/tree/master/data_collection).  View the scraped data in [our Google Drive](https://drive.google.com/drive/folders/1lgRqxc8dWflkXn8a2dRB8GBswCe_bZpZ), within the `images` folder, and our plant metadata within the `plant_meta` folder.

## Machine Learning

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiian Islands. For more details see [ohia.ai/machine_learning](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning).

## Results

|       Plant Name |     Top 1 Accuracy |     Top 3 Accuracy |     Top 5 Accuracy | Image Count |
| :--- | ---: | ---:  | ---: | ---: |
|         [Abutilon](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Abutilon)         |  80.55% |  83.33% |  88.88% |   374 |
|      [Achyranthes](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Achyranthes)      |  53.12% |  65.62% |  78.12% |   258 |
|        [Aleurites](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Aleurites)        |  46.66% |  80.00% |  86.66% |   176 |
|           [Ananas](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Ananas)           |  86.00% |  90.00% |  96.00% |   612 |
|        [Anthurium](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Anthurium)        |  73.91% |  97.10% |  97.10% |   758 |
|       [Artocarpus](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Artocarpus)       |  73.07% |  88.46% |  88.46% |   303 |
|          [Bonamia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Bonamia)          |  66.66% |  66.66% |  66.66% |    44 |
|    [Bougainvillea](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Bougainvillea)    |  96.36% | 100.00% | 100.00% |   663 |
|        [Canavalia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Canavalia)        |  62.50% |  79.16% |  83.33% |   212 |
|     [Chrysodracon](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Chrysodracon)     |  63.63% |  81.81% |  81.81% |   276 |
|            [Cocos](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Cocos)            |  83.87% |  90.32% |  93.54% |   311 |
|        [Colubrina](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Colubrina)        |  80.00% | 100.00% | 100.00% |    67 |
|           [Cordia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Cordia)           |  36.00% |  64.00% |  72.00% |   209 |
|        [Cordyline](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Cordyline)        |  82.75% | 100.00% | 100.00% |   335 |
|       [Cortaderia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Cortaderia)       |  50.00% | 100.00% | 100.00% |    39 |
|          [Cyperus](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Cyperus)          |  78.57% |  91.83% |  94.89% |   871 |
|         [Delairea](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Delairea)         |  71.42% | 100.00% | 100.00% |   111 |
|        [Dioscorea](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Dioscorea)        |  57.14% |  80.00% |  85.71% |   261 |
|          [Gouania](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Gouania)          |  66.66% |  66.66% |  66.66% |    31 |
|        [Heliconia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Heliconia)        |  87.71% |  94.73% |  98.24% |   622 |
|         [Hibiscus](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Hibiscus)         |  77.82% |  91.63% |  95.39% | 2,151 |
|        [Ischaemum](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Ischaemum)        |  50.00% |  75.00% |  75.00% |    41 |
|      [Isodendrion](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Isodendrion)      |  00.00% |  50.00% |  50.00% |    20 |
|         [Marsilea](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Marsilea)         |  75.00% | 100.00% | 100.00% |    51 |
|       [Mezoneuron](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Mezoneuron)       | 100.00% | 100.00% | 100.00% |    18 |
|     [Nothocestrum](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Nothocestrum)     |  37.50% |  50.00% |  75.00% |    64 |
|       [Officinale](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Officinale)       |  66.00% |  82.00% |  88.00% |   556 |
|          [Panicum](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Panicum)          |  58.06% |  90.32% |  98.38% |   580 |
|       [Pennisetum](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Pennisetum)       |  83.33% | 100.00% | 100.00% |   162 |
|       [Peucedanum](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Peucedanum)       |  00.00% |  50.00% |  50.00% |    31 |
|         [Plumeria](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Plumeria)         |  79.20% |  89.10% |  91.08% |   741 |
|        [Portulaca](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Portulaca)        |  61.84% |  82.89% |  82.89% |   623 |
|      [Pritchardia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Pritchardia)      |  84.61% |  96.15% |  98.07% |   464 |
| [Pseudognaphalium](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Pseudognaphalium) |  66.66% |  85.18% |  94.44% |   420 |
|            [Rubus](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Rubus)            |  84.56% |  93.95% |  97.31% | 1,113 |
|         [Scaevola](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Scaevola)         |  70.66% |  84.00% |  90.66% |   689 |
|         [Schenkia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Schenkia)         |  12.50% |  50.00% |  62.50% |    48 |
|          [Senecio](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Senecio)          |  80.80% |  92.92% |  94.94% |   854 |
|         [Sesbania](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Sesbania)         |  60.00% |  80.00% |  80.00% |   104 |
|    [Tetramolopium](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Tetramolopium)    |  65.00% |  90.00% |  95.00% |   146 |
|       [Tibouchina](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Tibouchina)       |  33.33% | 100.00% | 100.00% |    26 |
|            [Vigna](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Vigna)            |  50.00% |  68.75% |  75.00% |   101 |


## Usage

### Easy to follow steps.
<p align="center"> <img src="/figures/screenshots/screenshot2.jpg?raw=true"> </p>

### Look up info on the plants of Hawai'i.
<p align="center"> <img src="/figures/screenshots/screenshot3.jpg?raw=true"> </p>

### Detailed info and story on native plants.
<p align="center"> <img src="/figures/screenshots/screenshot1.jpg?raw=true"> </p>    

### Historical uses of plants and gallery of uploaded images.
<p align="center"> <img src="/figures/screenshots/screenshot4.jpg?raw=true"> </p>
