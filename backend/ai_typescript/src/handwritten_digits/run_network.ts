import * as tf from '@tensorflow/tfjs-node';
import * as path from 'path';

const modelPath = path.join(__dirname, '..', '..', '..', '..', 'models');
const model = tf.loadLayersModel('file://' + modelPath + '/num_reader/num_reader.json');

const picturePath = path.join(__dirname, '..', '..', 'pictures');
const img = new Image();
img.src = picturePath + '/num_bad/2.png';

