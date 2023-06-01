from Layer import NeuronLayer
import numpy as np
# Crear capa oculta con 2 neuronas
hidden_layer = NeuronLayer(2, 2, 'sigmoid')

# Crear capa de salida con 1 neurona
output_layer = NeuronLayer(1, 2, 'sigmoid')

# Datos de entrenamiento
training_data = [
    {'inputs': np.array([0, 0]), 'output': 0},
    {'inputs': np.array([0, 1]), 'output': 1},
    {'inputs': np.array([1, 0]), 'output': 1},
    {'inputs': np.array([1, 1]), 'output': 0},
]

# Entrenamiento
epochs = 10000
learning_rate = 0.01

for i in range(epochs):
    for data in training_data:
        # Propagación hacia adelante
        hidden_layer_output = hidden_layer.forward(data['inputs'])
        output_layer_output = output_layer.forward(hidden_layer_output)
        #print(f"Input: {data['inputs']}, Output: {output_layer_output}, hidden_layer_output: {hidden_layer_output}")

        # Cálculo del error y retropropagación
        output_error = data['output'] - output_layer_output[0]
        partial_derivative_output = output_layer_output[0] * (1 - output_layer_output[0])
        output_delta = output_error * partial_derivative_output
        hidden_error = output_delta * output_layer.neurons[0].weights
        partial_derivative_hidden = hidden_layer_output * (1 - hidden_layer_output)
        hidden_delta = hidden_error * partial_derivative_hidden

        # Actualización de pesos
        output_layer.neurons[0].weights += learning_rate * output_delta * hidden_layer_output
        output_layer.neurons[0].bias += learning_rate * output_delta
        #print(f"output_error: {output_error}")
        hidden_layer.neurons[0].weights += learning_rate * hidden_delta * data['inputs'][0]
        hidden_layer.neurons[1].weights += learning_rate * hidden_delta * data['inputs'][1]
        hidden_layer.neurons[0].bias += learning_rate * hidden_delta[0]
        hidden_layer.neurons[1].bias += learning_rate * hidden_delta[1]

# Prueba
for data in training_data:
    input_data = data['inputs']
    target_output = data['output']

    hidden_layer_output = hidden_layer.forward(input_data)
    output_layer_output = output_layer.forward(hidden_layer_output)

    output = output_layer_output[0]
    print(f"Input: {input_data}, Output: {output}, Target Output: {target_output}")
