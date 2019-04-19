import tensorflow as tf
import keras.preprocessing.image as image
import cv2
import matplotlib.pyplot as plt


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
model.fit(training_images, training_labels, epochs=20)
