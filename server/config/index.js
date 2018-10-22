const { env } = process;
const config = {
  credentials: {
    accessKeyId: env.AWS_ACCESS_KEY_ID,
    secretAccessKey: env.AWS_SECRET_ACCESS_KEY,
  },
  region: env.AWS_REGION,
  bucket: env.AWS_BUCKET,
};

module.exports = config;
