import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, input_dim=2, activation='tanh'),
    tf.keras.layers.Dense(1, activation='tanh')
])

input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = np.array([[0], [1], [1], [0]])

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(input, output, epochs=1000)

print(model.predict(input))

x = np.linspace(-0.25, 1.25, 100)
(X1_raster, X2_raster) = np.meshgrid(x, x)
X1_vektor = X1_raster.flatten()
X2_vektor = X2_raster.flatten()

input_graphic = np.vstack((X1_vektor, X2_vektor)).T
output_grpahic = model.predict(input_graphic).reshape(X1_raster.shape)

(weights, bias) = model.layers[0].get_weights()

plt.contourf(X1_raster, X2_raster, output_grpahic, 100)
plt.xlim(-0.25, 1.25)
plt.ylim(-0.25, 1.25)
plt.xlabel("Input $x_1$")
plt.ylabel("Input $x_2$")
plt.colorbar()

plt.scatter(np.array([0, 0, 1, 1]), np.array([0, 1, 0, 1]), color="red")

for i in range(2):
    plt.plot(x, -weights[0, i] / weights[1, i] * x - bias[i]/weights[1, i], color="black")

plt.show()
