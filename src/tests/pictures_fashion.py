import tensorflow as tf
import keras.preprocessing.image as image
import cv2
import os
from os.path import abspath
import matplotlib.pyplot as plt
import numpy as np

# Init Network and train it

# 0: T-Shirt
# 1: Trouser
# 2: Pullover
# 3: Dress
# 4: Coat
# 5: Sandal
# 6: Shirt
# 7: Sneaker
# 8: Bag
# 9: Ankle boot

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0

test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model = tf.keras.models.Sequential([

    # For pictures -> 2D Pictures in 1D Data
    tf.keras.layers.Flatten(),

    # 128 Neurons
    # Relu: Linear above 0
    tf.keras.layers.Dense(128, activation='relu'),

    # 10 Neurons
    # Softmax: Probability, sum of all neurons = 1
    tf.keras.layers.Dense(10, activation='softmax'),
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)


# Load pictures for testing

try:
    path = abspath('src/pictures/fashion/shoe.jpg')
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
x = x.reshape((1, 28, 28, 1))

plt.imshow(img, cmap='Greys_r')
plt.show()

classes = model.predict(x)
plt.bar(range(10), classes[0])
plt.show()
print('Prediction: class ', np.argmax(classes[0]))
