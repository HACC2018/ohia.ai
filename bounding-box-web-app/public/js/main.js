window.onload = function() {
  var video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  var context = canvas.getContext('2d');
  var tracker = new tracking.ObjectTracker('face');
  tracker.setInitialScale(4);
  tracker.setStepSize(2);
  tracker.setEdgesDensity(0.1);
  // tracking.track('#video', tracker, { camera: true });
  // tracker.on('track', function(event) {
  //   context.clearRect(0, 0, canvas.width, canvas.height);
  //   event.data.forEach(function(rect) {
  //       context.strokeStyle = '#a64ceb';
  //       context.strokeRect(rect.x, rect.y, rect.width, rect.height);
  //       context.font = '11px Helvetica';
  //       context.fillStyle = "#fff";
  //       context.fillText('x: ' + rect.x + 'px', rect.x + rect.width + 5, rect.y + 11);
  //       context.fillText('y: ' + rect.y + 'px', rect.x + rect.width + 5, rect.y + 22);
  //       context.fillText('Human detected', rect.x + rect.width + 5, rect.y + 33);
  //       context.fillText('Terminate immediately', rect.x + rect.width + 5, rect.y + 44)
  //   });
  // });


  const MODEL_URL = 'js/data/model/optimized_model.pb';
  const WEIGHTS_URL = 'js/data/model/weights_manifest.json';
  const model = tf.loadFrozenModel(MODEL_URL, WEIGHTS_URL).then((loadedModel) => {
            var MyTracker = function() {
              MyTracker.prototype.track = function(pixels, width, height) {
                // Your code here
                // console.log(pixels)
                
                // create off-screen canvas element
                let canvas_ = document.createElement('canvas'),
                ctx = canvas_.getContext('2d');
                canvas_.width = canvas.width;
                canvas_.height = canvas.height;
                // create imageData object
                let idata = ctx.createImageData(canvas.width, canvas.height);
                // set our buffer as source
                idata.data.set(pixels);
                
                
                let tensor = tf.fromPixels(idata)
                            .resizeNearestNeighbor([224, 224])
                            .toFloat()
                const offset = tf.scalar(127.5)
                tensor       = tensor.sub(offset)
                                .div(offset)
                                .expandDims();

                const predictions = loadedModel.predict(tensor);

                let top5 = Array.from(predictions.data)
                                .map(function(p) {
                                    var test = "hello"
                                    return {
                                      probability: p
                                      // className: IMAGENET_CLASSES[i]
                                    };
                                }).sort(function(a, b) {
                                  return b.probability - a.probability;
                                }).slice(0, 5);
                top5.forEach(function(p) {
                  console.log(p.className)
                })
                // this.emit('track', {
                //   // Your results here
                //   test: "hello"
                // });
              }
            }
            tracking.inherits(MyTracker, tracking.Tracker);
            var test = new MyTracker();
            // test.on('track', function(event) {
            //   console.log("got something")
            // });
            tracking.track('#video', test, { camera: true });
  });

 


   // Define a model for linear regression.

  //  const model = tf.sequential();
  //  model.add(tf.layers.dense({units: 1, inputShape: [1]}));

  //  // Prepare the model for training: Specify the loss and the optimizer.
  //  model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

  //  // Generate some synthetic data for training.
  //  const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
  //  const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

  //  // Train the model using the data.
  //  model.fit(xs, ys, {epochs: 10}).then(() => {
  //    // Use the model to do inference on a data point the model hasn't seen before:
  //    // Open the browser devtools to see the output
  //    model.predict(tf.tensor2d([5], [1, 1])).print();
  //  });

//   var gui = new dat.GUI();
//   gui.add(tracker, 'edgesDensity', 0.1, 0.5).step(0.01);
//   gui.add(tracker, 'initialScale', 1.0, 10.0).step(0.1);
//   gui.add(tracker, 'stepSize', 1, 5).step(0.1);
};