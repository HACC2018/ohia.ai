/*
  Based on code from:
    http://jamesthom.as/blog/2018/08/07/
    machine-learning-in-node-dot-js-with-tensorflow-dot-js/
*/

const fs = require('fs');
const path = require('path');
const jpeg = require('jpeg-js');

// Load the core TensorFlow.js library
const tf = require('@tensorflow/tfjs');
// Load the Node CPU bindings
require('@tensorflow/tfjs-node');
// Load the MobileNet pretrained model
const mobilenet = require('@tensorflow-models/mobilenet');

// Load models from the filesystem
const modelPath = path.resolve(__dirname, 'models', 'mobilenet', 'model.json');
// MobileNet model has 3 color channels
const NUMBER_OF_CHANNELS = 3;

const readImage = (imagePath) => {
  const buffer = fs.readFileSync(imagePath);
  return decodeBuffer(buffer);
};

const decodeBuffer = (buffer) => {
  // Return a `Uint8Array` with 4 channel values (RGBA) for each pixel
  return jpeg.decode(buffer, true);
};

// Convert the 4-channel array into a 3-channel version
const convertImageToByteArray = (image, numChannels) => {
  const pixels = image.data;
  const numPixels = image.width * image.height;
  const values = new Int32Array(numPixels * numChannels);

  for (let i = 0; i < numPixels; i++) {
    for (let channel = 0; channel < numChannels; ++channel) {
      values[i * numChannels + channel] = pixels[i * 4 + channel];
    }
  }
  return values;
};

const convertImageToInput = (image, numChannels) => {
  const values = convertImageToByteArray(image, numChannels);
  const outShape = [image.height, image.width, numChannels];
  return tf.tensor3d(values, outShape, 'int32');
};

const loadModel = async (modelPath) => {
  // Manually create the MobileNet class
  const model = new mobilenet.MobileNet(1, 1);
  // Overwrite the HTTP address of the model with a local filesystem path
  model.path = `file://${modelPath}`;
  await model.load();
  return model;
};

const detectPlant = async (modelPath, imageBuffer) => {
  const image = decodeBuffer(imageBuffer);
  const input = convertImageToInput(image, NUMBER_OF_CHANNELS);

  const model = await loadModel(modelPath);
  const predictions = await model.classify(input);
  return predictions;
};

module.exports = {
  detectPlant(imageBuffer) {
    return detectPlant(modelPath, imageBuffer);
  },
};
