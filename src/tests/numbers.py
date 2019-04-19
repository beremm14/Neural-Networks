import tensorflow as tf
from tensorflow import keras

network = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

network.compile(optimizer='sgd', loss='mean_squared_error')

xs=[1, 2, 3]
ys=[2, 4, 6]

network.fit(xs, ys, epochs=1000)

print(network.predict([1000]))
