# Feed Forward Neural Network using NumPy

import numpy as np

# Input data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Weights for input to hidden layer
weights_input_hidden = np.array([[0.5, 0.3],
                                 [0.4, 0.7]])

# Weights for hidden to output layer
weights_hidden_output = np.array([[0.6],
                                  [0.9]])

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Feed Forward Process

# Hidden layer
hidden_input = np.dot(X, weights_input_hidden)
hidden_output = sigmoid(hidden_input)

# Output layer
final_input = np.dot(hidden_output, weights_hidden_output)
final_output = sigmoid(final_input)

print("Output of Feed Forward Neural Network:")
print(final_output)
