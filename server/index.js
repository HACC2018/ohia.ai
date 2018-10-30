const express = require('express');
const AWS = require('aws-sdk');
const fs = require('fs');
const path = require('path');
const config = require('./config');
const knex = require('knex')({
  client: 'pg',
  connection: {
    host: config.db.host,
    user: config.db.username,
    password: config.db.password,
    database: 'ohia_db_dev',
    charset: 'utf8',
  },
});
const bookshelf = require('bookshelf')(knex);

const app = express();
const s3 = new AWS.S3({
  apiVersion: '2006-03-01',
});
const port = 3000;

function initializeServices() {
  const awsConfig = new AWS.Config({
    credentials: config.credentials,
    region: config.region,
  });
}

app.get('/', (req, res) => {
  res.send('Hello ohia.ai');
});

app.post('/images/upload', (req, res) => {
  const keyName = 'ohia_lehua.jpg';
  const params = {
    Bucket: config.bucket,
    Key: keyName,
    // TODO: This will need to change to accommodate images from the frontend.
    Body: fs.createReadStream(path.resolve(__dirname, `images/${keyName}`)),
    ACL: 'public-read',
  };

  s3.upload(params, (err, data) => {
    if (err) {
      console.error(err);
      return res.json({
        success: false,
      });
    }
    console.log('Successfully uploaded data to the S3 bucket');
    res.json({
      success: true,
      imageUrl: data['Location'],
    });
  });
});

app.listen(port, () => {
  console.log(`Server for ohia.ai listening on port ${port}`);
  initializeServices();
});
