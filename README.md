# ohia.ai

An open Hawaiian indigenous plant identification and aggregation application. Developed for the 2018 Hawaii Annual Code Challenge.

## Database

### Seed Plant Data
1. Download a copy of the `plant_meta_vX.csv` from our Google Drive and delete columns after the `updated_at` column.
    1. File > Download as > Comma-separated values
1. Connect to the database and enter the password when prompted:
    ```
    psql -d PG_NAME -U PG_USERNAME -h PG_HOST -p PG_PORT
    ```
1. Run the following command to seed the `plants` table:
    ```
    \copy plants FROM '/absolute/path/to/plant_meta_vX.csv' delimiter ',' csv header
    ```


## Data Collection

Machine learning involves learning from data, thus data collection is an integral part of our application.  The following is summary of the data that our team collected.

| Source | Preprocessing | Image Count | Number of Classes (Plants) |
| -------| ------------- |----------------- | -------------------------- |
| Scraped | None | 21,070 | 42 |
| Scraped | Removed non-plant images | 17,263 | 42 |
| PlantNet | None | 264,795 | 9,968 |
| PlantNet | Removed species with fewer than 100 images | 81,834 | 436 |
| ImageNet | None | 1,281,167 | 1000 |

For more details see [ohia.ai/data_collection](https://github.com/HACC2018/ohia.ai/tree/master/data_collection).

## Machine Learning

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiian Islands. For more details see [ohia.ai/machine_learning](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning).

## Results


|       Plant Name |     Top 1 Accuracy |     Top 3 Accuracy |     Top 5 Accuracy | Image Count |
| --- | --- | --  | --- | --- |
|         [Abutilon](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Abutilon)         |  80.55% |  83.33% |  88.88% |   374 |
|      [Achyranthes](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Achyranthes)      |  53.12% |  65.62% |  78.12% |   258 |
|        [Aleurites](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Aleurites)        |  46.66% |  80.00% |  86.66% |   176 |
|           [Ananas](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Ananas)           |  86.00% |  90.00% |  96.00% |   612 |
|        [Anthurium](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Anthurium)        |  73.91% |  97.10% |  97.10% |   758 |
|       [Artocarpus](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Artocarpus)       |  73.07% |  88.46% |  88.46% |   303 |
|          [Bonamia](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Bonamia)          |  66.66% |  66.66% |  66.66% |    44 |
|    [Bougainvillea](https://github.com/HACC2018/ohia.ai/tree/master/machine_learning/results/Bougainvillea)    |  96.36% |  00.00% | 100.00% |   663 |
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
