import numpy as np

inputs = np.array([5, 8])
print("Input:", inputs)

# We have 3 neurons in the hidden layer.Each row represents the weights of one neuron.
weights = np.array([
    [0.5, 0.2],   # Neuron 1
    [0.8, 0.4],   # Neuron 2
    [0.3, 0.9]    # Neuron 3
])

# One bias for each neuron

bias = np.array([0.1, 0.2, 0.3])

# sigmoid func
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# z = wx + b
z_hidden = np.dot(weights, inputs) + bias
print("\nHidden Layer Z:")
print(z_hidden)

# Apply activation function
output = sigmoid(z_hidden)
print("\nHidden Layer Output:")
print(output)

# Hidden layer has 3 outputs, therefore output neuron has 3 weights.
weights_output = np.array([0.7, 0.5, 0.2])
bias_output = 0.1

z_output = np.dot(weights_output,output) + bias_output
print("\nOutput Layer Z:")
print(z_output)

prediction = sigmoid(z_output)
print("\nFinal Prediction:")
print(prediction)


















