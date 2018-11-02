
// code modifiedd from https://github.com/tensorflow/tfjs-examples/tree/master/mobilenet
const fs = require('fs');
const path = require('path');
const jpeg = require('jpeg-js');

// Load the core TensorFlow.js library
const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

// load dictionary mapping plant_ids to plant_names
const PLANTNET_CLASSES = require('./models/mobilenetv1-1.00/plantnet_classes');
// const PLANTNET_CLASSES = require('./models/nasnetmobile/plantnet_classes');


// set parameters
const TOPK = 10;
const IMAGE_SIZE = 224;
const NUMBER_OF_CHANNELS = 3;
// const MODEL_PATH = 'file://' + path.resolve(__dirname, 'models', 'nasnetmobile', 'model.json'); 
const MODEL_PATH = 'file://' + path.resolve(__dirname, 'models', 'mobilenetv1-1.00', 'model.json'); 


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
  // const image_data =  new ImageData(image.data, image.width, image.height)
  // let input = tf.fromPixels(image_data, shape, 'float32');
  const values = convertImageToByteArray(image);
  const shape = [1, image.height, image.width, NUMBER_OF_CHANNELS];
  let input = tf.tensor4d(values, shape, 'float32');
  input = tf.image.resizeBilinear(input, [224, 224]);
  input = input.mul(tf.scalar(1/255.));
  input = tf.scalar(-1).add(input);
  return input
};

// computes topK probabilities and corresponding classes
const getTopK = async (probabilities) => {

  // get sorted (descending) probabilities and indexes
  const probsAndIndexs = [];
  for (let i = 0; i < probabilities.length; i++) {
    probsAndIndexs.push({prob: probabilities[i], index: i});
  }
  probsAndIndexs.sort((a, b) => {
    return b.prob - a.prob;
  });

  // get top k locations and labels
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
}


// put it all together to detect plant
const detectPlant = async (imagePath) => {
  const image = readImage(imagePath);
  const input = convertImageToInput(image);

  const model = await tf.loadModel(MODEL_PATH);
  const probabilities = model.predict(input).dataSync();
  console.log('Identification Results:', getTopK(probabilities));
};



// const imagePath = path.resolve(__dirname, 'images', 'albutilon.jpg');
const imagePath = path.resolve(__dirname, 'images', 'bougainvillia.jpg');
// const imagePath = path.resolve(__dirname, 'images', 'mug.jpeg');

detectPlant(imagePath);

