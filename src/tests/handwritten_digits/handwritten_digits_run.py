import tensorflow as tf
import keras.preprocessing.image as image
import cv2
import os
from os.path import abspath
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import io

model = tf.keras.models.load_model('models/num_reader.model')

# Load pictures for testing

path = abspath('src/pictures/2.jpg')
print(path)
img = io.imread(path, as_gray=True)

img = cv2.resize(img, (28, 28))
IMG = np.reshape(img, (1, 784))

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = image.img_to_array(IMG, dtype=np.float32)

if np.any(x[0,0]>250):
    print("Inverting the picture")
    x -= 255
    x *= -1

x = x/255.0

plt.imshow(img, cmap='Greys_r')
plt.show()

numbers = model.predict(x)
plt.bar(range(10), numbers[0])
plt.show()
print('Prediction: Number ', np.argmax(numbers[0]))
