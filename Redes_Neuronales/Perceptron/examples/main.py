import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from perceptron import Perceptron

# generate synthetic dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                            n_redundant=0, n_clusters_per_class=1, random_state=42)

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create perceptron object
perceptron = Perceptron()

# train perceptron on training data
perceptron.fit(X_train, y_train)

# make predictions on testing data
y_pred = perceptron.predict(X_test)
print(f"Predictions: {y_pred}")

# compute accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# plot decision boundary
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 100), np.linspace(ylim[0], ylim[1], 100))
Z = perceptron.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contourf(xx, yy, Z, alpha=0.2, cmap='bwr')
plt.show()
