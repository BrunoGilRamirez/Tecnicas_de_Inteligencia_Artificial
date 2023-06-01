import numpy as np

class neurona:
    def __init__(self, num_inputs, activation='sigmoid'): # Constructor
        np.random.seed(42)
        self.weights = np.random.rand(num_inputs)   # Pesos
        self.bias = np.random.rand() # Bias
        self.activation = activation # Función de activación
        self.activation_fn = self._get_activation_fn() # Función de activación
    
    def _get_activation_fn(self):
        if self.activation == 'sigmoid':
            return lambda x: 1 / (1 + np.exp(-x)) # Función sigmoide
        elif self.activation == 'relu':
            return lambda x: np.maximum(0, x) # Función relu
        elif self.activation == 'tanh':
            return lambda x: np.tanh(x) # Función tangente hiperbólica
        
    
    def forward(self, inputs): # Propagación hacia adelante                                                                           
        linear_output = np.dot(inputs, self.weights) + self.bias # se calcula la salida lineal
        Actnet =self.activation_fn(linear_output)
        return Actnet # se calcula la salida de la neurona
    
    def _get_activation_gradient(self, output): # Derivada de la función de activación (para backpropagation)
        if self.activation == 'sigmoid':
            return output * (1 - output) # Derivada de la función sigmoide
        elif self.activation == 'relu':
            return np.where(output > 0, 1, 0) # Derivada de la función relu
        elif self.activation == 'tanh':
            return 1 - output ** 2 # Derivada de la función tangente hiperbólica
    
    def train(self, inputs, target_output, learning_rate):
        output = self.forward(inputs) # se obtiene el valor de salida de la neurona
        error = target_output - output # se calcula el error, que es la diferencia entre el valor esperado y el valor obtenido
        activation_gradient = self._get_activation_gradient(output) # se calcula la derivada de la función de activación
        gradient = error * activation_gradient # se calcula el gradiente, el gradiente se usa para actualizar los pesos y el bias
        weights_delta = learning_rate * gradient * inputs # se calcula el cambio en los pesos
        bias_delta = learning_rate * gradient # se calcula el cambio en el bias
        self.weights += weights_delta # se actualizan los pesos
        self.bias += bias_delta # se actualiza el bias