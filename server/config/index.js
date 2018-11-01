require('dotenv').config();

const { env } = process;

const config = {
  credentials: {
    accessKeyId: env.AWS_ACCESS_KEY_ID,
    secretAccessKey: env.AWS_SECRET_ACCESS_KEY,
  },
  region: env.AWS_REGION,
  bucket: env.AWS_BUCKET,
  db: {
    host: env.PG_HOST,
    port: env.PG_PORT,
    name: env.PG_NAME,
    username: env.PG_USERNAME,
    password: env.PG_PASSWORD
  }
};

module.exports = config;
