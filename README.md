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
    
## Machine Learning

Behind the scenes, ohia.ai is powered by machine learning and AI.  Our team utilizes modern deep learning techniques and large open source datasets to achieve highly accurate classification on a wide range of flora found throughout the Hawaiiain Islands.

To run our custom models:
1. Preprocess data using `python machine_learning/preprocess.py`. 
2. Train models using `python machine_learning/train.py`.  

See our `machine_learning/README.md` for more details.