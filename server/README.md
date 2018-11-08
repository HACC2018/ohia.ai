# ohia.ai API Server

## Table of Contents

* [Requirements](#requirements)
* [Installation and Execution](#installation-and-execution)
    * [If deploying the client to an iOS device](#if-deploying-the-client-to-an-ios-device)
* [Deployment](#deployment)
* [Known Server Issues](#known-server-issues)
* [Seeding the Database](#seeding-the-database)

## Requirements

1. [Python](https://www.python.org/) version 2.7.x
1. [Node.js](https://nodejs.org/en/) version 10.12.0

## Installation and Execution

1. If you haven't already, switch your terminal to [use Python 2.7](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-python-required) and [Node 10.12.0](https://github.com/HACC2018/ohia.ai/blob/master/client/README.md#install-nodejs-required).
1. Perform all of the following steps from the project root directory.
1. Run `npm install`. Among other items, you should see "Downloading libtensorflow" and "Building TensorFlow Node.js bindings" run without error in your output.
1. Create a `.env` file by copying the template in `.env.sample`.
1. Source your environment by running: `source .env`.
1. You should now see these variables in your environment by running `env`.
1. Add the machine learning model weight files from [our Google Drive](https://drive.google.com/drive/folders/1rOyizBeTlXasRRi34Coasr-TJgtJatHz) by first downloading and unzipping `weights.tar.gz` using the command `tar xzf weights.tar.gz`, followed by replacing the `/server/models/mobilenetv1-1.00` folder with the respective unzipped folder.
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
    
### If deploying the client to an iOS device
1. You might want to install ngrok via `npm install -g ngrok`.
1. Once installed, you can run `ngrok http 3000` to have a random URL, such as `https://ef7107dd.ngrok.io`, point to your `http://localhost:3000` server for a full 8 hours. Note that you can keep ngrok up, even if you stop or restart your Node server.
1. Be sure to change `API_HOST` in your `.env` file to `https://ef7107dd.ngrok.io` (whatever the URL is), and then re-source it with `source .env` before running `npm run dev-server` again.
1. Note that you should also re-source your environment in the terminal window for building the client code, before running `npm run prod-ios` again.
    
## Deployment

1. Create an Amazon S3 bucket that enables public images.
1. Create a PostgreSQL RDS instance with the following specs:
    ```
    - 20 GiB storage
    - PostgreSQL 10.5-R1
    - db.t2.micro -- 1 vCPU, 1GiB RAM
    - DB instance identifier: ohia-db-dev
    - Public accessibility: Yes
    - Availability zone: us-west-2a
    - VPC security groups: default (actually ohia-public-sg-prod)
    ```
1. Create an EC2 instance and install Node, `git`, `nginx`, and `pm2` to it.
1. Fork this repository and clone the fork to the EC2 server.
1. Install the project on the server, set up nginx, and run the Node server as a pm2 process.

## Known Server Issues

When running `pm2 logs` on the EC2 server:
- There are errors about the port being in use, yet the API server is still accessible via Postman or the ohia.ai app:
    ```
    Error: listen EADDRINUSE :::3000
    ```
- There are errors about the bucket being required, but images nevertheless get uploaded to S3:
    ```
    Error: bucket is required
    0|index  |     at new S3Storage (/home/ec2-user/ohia.ai/node_modules/multer-s3/index.js:84:29)
    ```
- There are `tfjs-node` errors, even if the model is able to make predictions and return them to the client:
    ```
    Registration of backend tensorflow failed
    2|index  | Error: /home/ec2-user/ohia.ai/node_modules/@tensorflow/tfjs-node/build/Release/tfjs_binding.node: invalid ELF header
    ```
- The server keeps exiting and restarting:
    ```
    App [index:2] exited with code [1] via signal [SIGINT]
    PM2      | App [index:2] starting in -fork mode-
    ```

## Seeding the Database

Perform all of the following steps from the project root directory.

### Only During Development: Drop and Restore the Database
1. If you would like to delete the database, run: `npm run db:rollback`.
1. Then, run the following to restore the database: `npm run db:migrate`.

### Seeding Plant and Image Data
1. Create database tables if you haven't already: `npm run db:migrate`.
1. Download a copy of the `plant_meta_vX.csv` from [our Google Drive](https://drive.google.com/drive/folders/1tH7L96inE8mpNV9dcm7nkPieXd7f4DYZ) (where **X** is the latest version number) and delete columns after the `updated_at` column (if any).
    1. Open it in Google Sheets and go to File > Download as > Comma-separated values.
1. Download a copy of the `plant_images_vY.csv` from [our Google Drive](https://drive.google.com/drive/folders/1tH7L96inE8mpNV9dcm7nkPieXd7f4DYZ) (where **Y** is the latest version number).
1. Connect to the database and enter the password when prompted:
    ```
    psql -d PG_NAME -U PG_USERNAME -h PG_HOST -p PG_PORT
    ```
1. Run the following command to seed the `plants` table:
    ```
    \copy plants FROM '/absolute/path/to/plant_meta_vX.csv' delimiter ',' csv header
    ```
    The expected output is `COPY 44`.
1. Run the following command to seed the `plant_images` table:
    ```
    \copy plant_images FROM '/absolute/path/to/plant_images_vY.csv' delimiter ',' csv header
    ```
    The expected output is `COPY 114`.
