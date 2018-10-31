const express = require('express');
const bodyParser = require('body-parser');
const AWS = require('aws-sdk');
const multer = require('multer');
const multerS3 = require('multer-s3');
const config = require('./config');

const app = express();
const s3 = new AWS.S3({
  apiVersion: '2006-03-01',
});

const PORT = 3000;
const FILE_SIZE_LIMIT = '50mb'; // Should match param limit
const PARAM_LIMIT = 50000; // In MB; should match file size limit

function initializeServices() {
  const awsConfig = new AWS.Config({
    credentials: config.credentials,
    region: config.region,
  });
}

const upload = multer({
  storage: multerS3({
    s3,
    bucket: config.bucket,
    acl: 'public-read',
    contentType: multerS3.AUTO_CONTENT_TYPE,
    // Tell browsers and CDNs to cache the file for one year
    cacheControl: 'max-age=31536000',
    metadata(req, file, cb) {
      cb(null, Object.assign({}, req.body));
    },
    key(req, file, cb) {
      // The file is always a JPEG
      const filename = `${Date.now().toString()}.jpg`;
      cb(null, filename);
    },
  }),
});

// Middleware
app.use(bodyParser.json({ // JSON request data
  limit: FILE_SIZE_LIMIT,
}));

app.use(bodyParser.urlencoded({ // Form request data
  extended: false,
  limit: FILE_SIZE_LIMIT,
  parameterLimit: PARAM_LIMIT,
})); 

// Routes
app.post('/images/upload', upload.array('image', 1), (req, res) => {
  console.log('req.body', req.body);
  console.log('req.files', req.files);
  const image = req.files.length > 0 ? req.files[0] : { key: '', size: 0 };
  return res.json({
    success: true,
    name: image.key,
    size: image.size,
  });
});

app.listen(PORT, () => {
  console.log(`Server for ohia.ai listening on port ${PORT}`);
  initializeServices();
});
