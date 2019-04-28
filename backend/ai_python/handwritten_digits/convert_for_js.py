import tensorflowjs as tfjs
import tensorflow as tf
import os
from os.path import abspath

def getHome():
    backend = os.path.dirname(os.getcwd())
    return os.path.dirname(backend)

model = tf.keras.models.load_model(abspath(getHome() + '/models/num_reader.h5'))
tfjs.converters.save_keras_model(model, abspath(getHome() + '/models/num_reader'))
