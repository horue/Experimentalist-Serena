from test2 import Preparer, Dataset
import tensorflow as tf
import numpy as np


xs = Preparer.tokenizeDataset()
ys = np.array(Dataset.datasetPoints, dtype=float)
print(xs)
print(xs.shape)

print(ys)

model = tf.keras.Sequential([

    # Define the input shape
    tf.keras.Input(shape=(9,)),

    # Add a Dense layer
    tf.keras.layers.Dense(units=4),
    tf.keras.layers.Dense(units=3),
    tf.keras.layers.Dense(units=2),
    tf.keras.layers.Dense(units=1, activation='sigmoid'),
])

model.compile(optimizer='adamw', loss='mse')
model.fit(xs, ys, epochs=250)


userInput = "estou feliz"
target = Preparer.tokenizeInput(userInput)
target = np.pad(target, 0, mode='constant')
print(target.shape)
print(target)


print(f"model predicted: {model.predict(target, verbose=0).item():.5f}")
