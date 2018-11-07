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

Machine learning involves learning from data, thus data collection is an integral part of our application.  Here is summary of the data that our team collected.

| Source | Preprocessing | Number of Images | Number of Classes (Plants) |
| -------| ------------- |----------------- | -------------------------- |
| Scraped | None | 21,070 | 42 |
| Scraped | Removed non-plant images | 17,263 | 42 |
| PlantNet | None | 264,795 | 9,968 |
| PlantNet | Removed species with fewer than 100 images | 81,834 | 436 |
| ImageNet | None | 1,281,167 | 1000 |

For more details see [ohia.ai/data_collection](https://github.com/HACC2018/ohia.ai/tree/master/data_collection).

## Machine Learning

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiian Islands.

For more details see [ohia.ai/machine_learning](https://github.com/HACC2018/ohia.ai/tree/master/data_collection).

## Results
