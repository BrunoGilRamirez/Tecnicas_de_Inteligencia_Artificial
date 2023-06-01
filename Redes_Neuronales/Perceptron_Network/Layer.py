from neurona import neurona as Neuron
import numpy as np
class NeuronLayer:
    def __init__(self, num_neurons, num_inputs, activation_func):
        self.num_neurons = num_neurons
        self.neurons = []
        for i in range(num_neurons):
            self.neurons.append(Neuron(num_inputs, activation_func))

    def forward(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.forward(inputs))
        return np.array(outputs)
