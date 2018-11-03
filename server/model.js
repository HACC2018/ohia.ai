/*
  Based on code from:
    http://jamesthom.as/blog/2018/08/07/
    machine-learning-in-node-dot-js-with-tensorflow-dot-js/
  With code modified from:
    https://github.com/tensorflow/tfjs-examples/tree/master/mobilenet
*/

const fs = require('fs');
const path = require('path');
const jpeg = require('jpeg-js');

// Load the core TensorFlow.js library
const tf = require('@tensorflow/tfjs');

// Load the Node CPU bindings
require('@tensorflow/tfjs-node');

// Load dictionary mapping plant_ids to plant_names
const PLANTNET_CLASSES = require('./models/mobilenetv1-1.00/plantnet_classes');

// Set parameters
const TOPK = 10;
const IMAGE_SIZE = 224;
const NUMBER_OF_CHANNELS = 3;

// Load model from the file system
const MODEL_PATH = 'file://' + path.resolve(__dirname, 'models', 'mobilenetv1-1.00', 'model.json'); 

// Return a `Uint8Array` with 4 channel values (RGBA) for each pixel
const decodeBuffer = (buffer) => {
  return jpeg.decode(buffer, true);
};

// Read image
const readImage = (imagePath) => {
  const buffer = fs.readFileSync(imagePath);
  return decodeBuffer(buffer);
};

// Convert the 4-channel array into a 3-channel version
const convertImageToByteArray = (image) => {
  const pixels = image.data;
  const numPixels = image.width * image.height;
  const values = new Int32Array(numPixels * NUMBER_OF_CHANNELS);

  for (let i = 0; i < numPixels; i++) {    
    for (let channel = 0; channel < NUMBER_OF_CHANNELS; ++channel) {  
      values[i * NUMBER_OF_CHANNELS + channel] = pixels[i * 4 + channel];
    }
  }
  return values;
};

// Convert to 4D tensor and resize to 1 x h x w x c
const convertImageToInput = (image) => {
  const values = convertImageToByteArray(image);
  const shape = [1, image.height, image.width, NUMBER_OF_CHANNELS];
  let input = tf.tensor4d(values, shape, 'float32');
  input = tf.image.resizeBilinear(input, [224, 224]);
  input = input.mul(tf.scalar(1/255.));
  input = tf.scalar(-1).add(input);
  return input
};

// Compute top K probabilities and corresponding classes
const getTopK = async (probabilities) => {
  // Get sorted (descending) probabilities and indexes
  const probsAndIndexs = [];
  for (let i = 0; i < probabilities.length; i++) {
    probsAndIndexs.push({ prob: probabilities[i], index: i });
  }
  probsAndIndexs.sort((a, b) => {
    return b.prob - a.prob;
  });

  // Get top K locations and labels
  const topkProbs  = new Float32Array(TOPK);
  const topkIndexs = new Int32Array(TOPK);
  for (let i = 0; i < TOPK; i++) {
    topkProbs[i]  = probsAndIndexs[i].prob;
    topkIndexs[i] = probsAndIndexs[i].index;
  }

  const topClassesAndProbs = [];
  for (let i = 0; i < topkIndexs.length; i++) {
    topClassesAndProbs.push({
      className: PLANTNET_CLASSES[topkIndexs[i]],
      probability: topkProbs[i]
    })
  }
  return topClassesAndProbs;
};

// Put it all together to detect the plant
const detectPlant = async (imageBuffer) => {
  const image = decodeBuffer(imageBuffer);
  const input = convertImageToInput(image);

  const model = await tf.loadModel(MODEL_PATH);
  const probabilities = model.predict(input).dataSync();
  return getTopK(probabilities);
};

module.exports = {
  detectPlant(imageBuffer) {
    return detectPlant(imageBuffer);
  },
};
