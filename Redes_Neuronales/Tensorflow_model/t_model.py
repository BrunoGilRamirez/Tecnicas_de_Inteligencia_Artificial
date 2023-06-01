import tensorflow as tf
import numpy as np

# Load the training data.
training_data = [
    {'inputs': np.array([0, 0]), 'output': 0},
    {'inputs': np.array([0, 1]), 'output': 1},
    {'inputs': np.array([1, 0]), 'output': 1},
    {'inputs': np.array([1, 1]), 'output': 0},
]
inputdata = [[0,0],[0,1],[1,0],[1,1]]
outputdata= [0,1,1,0]

# Create the model.
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, activation='relu', input_shape=(2,), use_bias=True,name="layer1"),
    tf.keras.layers.Dense(1, activation='step', name="layer2" )
])

# Compile the model.
model.compile(optimizer='adam', loss="binary_crossentropy" , metrics=['accuracy'])

# Train the model.
model.fit(inputdata, outputdata, epochs=10)

# Evaluate the model.
loss, accuracy = model.evaluate(inputdata, outputdata)
print('Loss:', loss)
print('Accuracy:', accuracy)

# Make predictions.
predictions = model.predict(inputdata)
print('Predictions:', predictions)
