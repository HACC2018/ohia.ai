
const fs = require('fs');
const path = require('path');
const jpeg = require('jpeg-js');

// Load the core TensorFlow.js library
const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

// load dictionary mapping plant_ids to plant_names
const PLANTNET_CLASSES = require('./models/plant_classes');

// set parameters
const TOPK = 10;
const IMAGE_SIZE = 224;
const NUMBER_OF_CHANNELS = 3;
const MODEL_PATH = 'file://' + path.resolve(__dirname, 'models', 'test_model', 'model.json');

// read image
const readImage = path => {
  const buf = fs.readFileSync(path)
  const pixels = jpeg.decode(buf, true)
  return pixels
}

// convert the 4-channel array into a 3-channel version
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

// convert to 4d tensor and resize to 1 x h x w x c
const convertImageToInput = (image) => {
  // const outShape = [1, image.height, image.width, NUMBER_OF_CHANNELS];
  // const input = tf.tensor4d(values, outShape, 'int32');

  const values = convertImageToByteArray(image);
  const shape = [1, image.height, image.width, NUMBER_OF_CHANNELS];
  let input = tf.tensor4d(values, shape, 'float32');
  input = tf.image.resizeBilinear(input, [224, 224]);
  input = input.mul(tf.scalar(1/255.))  
  return input
};


// computes topK probabilities and corresponding classes
const getTopK = async (predictions) => {
  // const values = await preds;

  // get sorted (descending) predictions and indexes
  const valuesAndIndices = [];
  for (let i = 0; i < predictions.length; i++) {
    valuesAndIndices.push({pred: predictions[i], index: i});
  }
  valuesAndIndices.sort((a, b) => {
    return b.pred - a.pred;
  });

  // 
  const topkValues = new Float32Array(TOPK);
  const topkIndices = new Int32Array(TOPK);
  for (let i = 0; i < TOPK; i++) {
    topkValues[i] = valuesAndIndices[i].pred;
    topkIndices[i] = valuesAndIndices[i].index;
  }

  const topClassesAndProbs = [];
  for (let i = 0; i < topkIndices.length; i++) {
    topClassesAndProbs.push({
      className: PLANTNET_CLASSES[topkIndices[i]],
      probability: topkValues[i]
    })
  }
  return topClassesAndProbs;
}


// put it all together to detect plant
const detectPlant = async (imagePath) => {
  const image = readImage(imagePath);
  const input = convertImageToInput(image);

  const model = await tf.loadModel(MODEL_PATH);
  const predictions = model.predict(input).dataSync();

  
  console.log('Identification Results:', getTopK(predictions));
};


// const imagePath = path.resolve(__dirname, 'images', 'flowers.jpg');
const imagePath = path.resolve(__dirname, 'images', 'mug.jpeg');
// const imagePath = path.resolve(__dirname, 'images', 'cat.jpg');
detectPlant(imagePath);

