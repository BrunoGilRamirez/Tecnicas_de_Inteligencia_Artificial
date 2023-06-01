import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1, num_epochs=100):
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1] + 1)  # add one for bias term
        for epoch in range(self.num_epochs):
            for xi, target in zip(X, y):
                # add bias term to input vector
                xi = np.concatenate((xi, [1]))
                activation = np.dot(xi, self.weights)
                # apply step function
                y_hat = 1 if activation > 0 else 0
                # update weights
                self.weights += self.learning_rate * (target - y_hat) * xi

    def predict(self, X):
        # add bias term to input vector
        X = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)
        # compute weighted sum and apply step function
        y_hat = np.where(np.dot(X, self.weights) > 0, 1, 0)
        return y_hat
