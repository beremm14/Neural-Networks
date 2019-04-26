import tensorflow as tf
import keras.preprocessing.image as image
import cv2
import os
from os.path import abspath
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import io

def getHome():
    backend = os.path.dirname(os.getcwd())
    return os.path.dirname(backend)


path = abspath(getHome() + '/models/num_reader.model')
print(path)
model = tf.keras.models.load_model(path)

try:
    path = abspath(getHome() + '/backend/pictures/num_bad/7.png')
    print(path)
    img = cv2.imread(path)
    if img == None:
        raise Exception('No image')
except Exception as ex:
    print(str(ex))


img = cv2.resize(img, (28, 28))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = image.img_to_array(img, dtype=np.float32)

if np.any(x[0,0]>250):
    print("Inverting the picture")
    x -= 255
    x *= -1

x = x/255.0
x = x.reshape(1, 28, 28, 1)

plt.imshow(img, cmap='Greys_r')
plt.show()

numbers = model.predict(x)
plt.bar(range(10), numbers[0])
plt.show()
print('\nPrediction: Number ', np.argmax(numbers[0]), '\n')
print('Predictions:')
print('0: ', numbers[0][0])
print('1: ', numbers[0][1])
print('2: ', numbers[0][2])
print('3: ', numbers[0][3])
print('4: ', numbers[0][4])
print('5: ', numbers[0][5])
print('6: ', numbers[0][6])
print('7: ', numbers[0][7])
print('8: ', numbers[0][8])
print('9: ', numbers[0][9])
