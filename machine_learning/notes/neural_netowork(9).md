# Neural Networks
A neural network is a machine learning model loosely inspired by how the human brain works. The brain contains billions of neurons connected to each other, passing signals back and forth to process information. A neural network borrows this idea and builds it in software using numbers and math.

The key thing that makes neural networks special is that they can **learn complex patterns automatically** from data without you manually engineering features. You feed in raw inputs, and the network figures out on its own what combinations of those inputs are meaningful.

They power almost everything impressive in modern AI: image recognition, language models, speech recognition, game playing, drug discovery, and much more.

---

## The Biological Inspiration

A biological neuron receives signals through dendrites, processes them in the cell body, and fires an output signal through the axon if the combined input is strong enough.

An artificial neuron mirrors this:

```
Inputs          Weights         Neuron          Output

x1 ----w1---->  |           |
x2 ----w2---->  |  sum + b  | --> activation --> ŷ
x3 ----w3---->  |           |
```

Each input $x$ is multiplied by a weight $w$, all the weighted inputs are summed together with a bias $b$, and the result is passed through an activation function to produce an output. That output becomes the input to the next layer.

---

## A Single Neuron - The Building Block
A single neuron computes:

$$
z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
$$

$$
a = g(z)
$$

Where:
- $z$ is the weighted sum (also called the pre-activation)
- $g$ is the activation function
- $a$ is the output of the neuron (also called activation)

This is exactly logistic regression if you use the sigmoid as $g$. In fact, logistic regression is just a single neuron with a sigmoid activation. A neural network is many of these neurons stacked together.

---

## Common Terms in Neural Networks
**Neuron (Node):** The basic unit. Takes inputs, computes a weighted sum, applies an activation function, outputs a value.

**Weight ($w$):** A learnable parameter that scales each input. The network adjusts weights during training to improve predictions.

**Bias ($b$):** A learnable offset added to the weighted sum. It allows the neuron to shift its activation even when all inputs are zero.

**Activation ($a$):** The output of a neuron after applying the activation function. It is what gets passed to the next layer.

**Activation Function ($g$):** A mathematical function applied to the weighted sum to introduce non-linearity. Without it, the entire network collapses to a single linear equation regardless of depth.

**Layer:** A group of neurons that all process inputs at the same level and pass their outputs to the next group.

**Parameters:** All the weights and biases in the network. These are what get learned during training.

**Hyperparameters:** Settings you choose before training — number of layers, number of neurons per layer, learning rate, activation function. They are not learned from data.

**Forward Pass:** The process of passing input through the network layer by layer to get a prediction.

**Loss:** How wrong a single prediction is.

**Cost:** Average loss across the entire training set.

**Epoch:** One full pass through the entire training dataset during training.

**Batch:** A subset of the training data used in one gradient descent update. Mini-batch training uses small batches (e.g. 32 or 64 examples) rather than the whole dataset at once.

---

## Layers — The Structure of a Neural Network

A neural network is organised into layers. Each layer transforms its inputs and passes the result to the next one.

### Input Layer

This is not really a layer that computes anything. It just holds the raw input features and passes them into the first real layer.

If your input has 4 features (house size, rooms, age, location score), the input layer has 4 nodes, one per feature.

### Hidden Layers

These are the layers between the input and output. They are called "hidden" because their values are not directly visible in the data  you do not observe them, the network creates them internally.

Hidden layers are where the magic happens. Each neuron in a hidden layer learns to detect some pattern or combination of the input features. Early hidden layers typically detect simple patterns. Deeper layers combine those simple patterns into more complex ones.

**Example in image recognition:**
- Layer 1 neurons learn to detect edges and corners
- Layer 2 neurons combine edges into shapes (circles, rectangles)
- Layer 3 neurons combine shapes into object parts (eyes, wheels, doors)
- Layer 4 neurons combine parts into full objects (face, car)

You did not tell the network to do this. It learned this hierarchy automatically from data.

### Output Layer

The final layer produces the network's prediction. The number of neurons and the activation function here depend on the task.

| Task | Output Neurons | Activation |
|------|---------------|-----------|
| Binary classification | 1 | Sigmoid (outputs probability 0 to 1) |
| Multi-class classification | One per class | Softmax (outputs probabilities summing to 1) |
| Regression | 1 | None or linear (outputs any real number) |

### Visualising the Structure

```
Input         Hidden         Hidden         Output
Layer         Layer 1        Layer 2        Layer

  x1  o                                        
       \       o   o                           
  x2  o  ---  o   o  ---   o   o  ---  o  -->  ŷ
       /       o   o                           
  x3  o                                        

4 inputs    4 neurons      3 neurons      1 output
```

Each line represents a weight connection. Every neuron in one layer connects to every neuron in the next layer. This is called a **fully connected** or **dense** layer.

---

## Activation Functions 

If there were no activation functions, each layer would just compute a linear transformation of the previous layer. A linear transformation of a linear transformation is still just a linear transformation. No matter how many layers you stack, the whole network would be equivalent to a single linear model  no better than linear regression.

Activation functions introduce **non-linearity**, which is what allows neural networks to model complex, curved, real-world patterns.

### Sigmoid

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Output range: 0 to 1. Used in the output layer for binary classification. Rarely used in hidden layers anymore because of the vanishing gradient problem (gradients become extremely small for large or small values of $z$, which slows learning in deep networks).

### Tanh (Hyperbolic Tangent)

$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

Output range: -1 to 1. Centred at zero, which makes it better than sigmoid for hidden layers. Still suffers from vanishing gradients for extreme values.

### ReLU (Rectified Linear Unit)

$$
g(z) = \max(0, z)
$$

Output: 0 if $z$ is negative, $z$ if $z$ is positive.


ReLU is the most widely used activation function in hidden layers today. It is simple, computationally cheap, and does not suffer from vanishing gradients for positive values. The main issue is "dying ReLU" where neurons can get stuck outputting zero if their weights push $z$ negative for all inputs.

### Leaky ReLU

$$
g(z) = \max(0.01z, z)
$$

A fix for dying ReLU. Instead of outputting exactly zero for negative $z$, it outputs a small negative value, keeping the gradient alive.

### Softmax

Used in the output layer for multi-class classification. Takes a vector of raw scores and converts them into probabilities that sum to 1.

$$
\text{softmax}(z_k) = \frac{e^{z_k}}{\sum_{j} e^{z_j}}
$$

If the model is classifying images into cat, dog, and bird, softmax might output [0.70, 0.25, 0.05] — 70% cat, 25% dog, 5% bird. The predicted class is the one with the highest probability.

### Which Activation to Use

| Location | Recommended Activation |
|----------|------------------------|
| Hidden layers (most cases) | ReLU |
| Hidden layers (some cases) | Leaky ReLU, Tanh |
| Output — binary classification | Sigmoid |
| Output — multi-class classification | Softmax |
| Output — regression | None (linear) |

---

## How a Neural Network Works - Forward Propagation

Forward propagation is the process of computing a prediction by passing the input through every layer one at a time from left to right.

### Notation

For a network with multiple layers, use superscripts in square brackets to denote the layer:

- $a^{[l]}$ is the activation of layer $l$
- $W^{[l]}$ is the weight matrix of layer $l$
- $b^{[l]}$ is the bias vector of layer $l$

### Step by Step

For a 3-layer network (2 hidden layers, 1 output layer):

**Layer 1:**
$$
Z^{[1]} = W^{[1]} X + b^{[1]}
$$
$$
A^{[1]} = g^{[1]}(Z^{[1]})
$$

**Layer 2:**
$$
Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]}
$$
$$
A^{[2]} = g^{[2]}(Z^{[2]})
$$

**Output Layer:**
$$
Z^{[3]} = W^{[3]} A^{[2]} + b^{[3]}
$$
$$
\hat{Y} = g^{[3]}(Z^{[3]})
$$

Each layer takes the previous layer's activations as input, computes a weighted sum, and applies an activation function. The final output $\hat{Y}$ is the network's prediction.

### A Concrete Example

A network predicting whether a customer will churn (1) or not (0).

Input features: account age, monthly spend, number of complaints, last login days ago.

```
Input:  [24, 85.5, 2, 7]   (account age, spend, complaints, days since login)

Layer 1: 4 inputs  →  3 neurons  →  ReLU  →  3 activations
Layer 2: 3 inputs  →  2 neurons  →  ReLU  →  2 activations
Output:  2 inputs  →  1 neuron   →  Sigmoid  →  probability of churn
```

Final output: 0.83 — the model predicts 83% probability the customer will churn.

---

## How the Network Learns 

Training a neural network involves three steps repeated many times:

**Step 1 — Forward pass:** Pass training examples through the network to get predictions.

**Step 2 — Compute cost:** Compare predictions to actual labels using a cost function (log loss for classification, MSE for regression).

**Step 3 — Backpropagation:** Compute how much each weight contributed to the error, then update all weights using gradient descent.

Backpropagation works by applying the chain rule of calculus to propagate error signals backwards through the network, from the output layer all the way back to the first hidden layer. This tells each weight: "you made the error larger" or "you made the error smaller" and by how much.

The weights are then nudged in the direction that reduces the cost. This whole cycle repeats for many epochs until the cost is minimised.

---

## Inference - Using a Trained Network

Inference is the term for using a trained neural network to make predictions on new data. It is just a forward pass — you feed in the input and the network outputs a prediction. No learning happens during inference, the weights stay fixed.

```
New input arrives
      |
      v
Forward pass through trained network
(weights are frozen, no updates)
      |
      v
Output: prediction or probability
      |
      v
Apply threshold or take argmax
      |
      v
Final class label or value
```

### Training vs Inference

| | Training | Inference |
|--|---------|---------|
| Data | Labelled training set | New, unseen data |
| Weights | Updated on every step | Frozen, no updates |
| Direction | Forward pass + backward pass | Forward pass only |
| Cost | Computed and minimised | Not needed |
| Speed | Slower (needs backprop) | Fast (forward only) |
| Hardware | GPU strongly preferred | CPU often sufficient |

Inference is much faster than training because there is no backpropagation happening. A model that took hours to train can make predictions in milliseconds.

---

## Architecture — Putting It All Together

The term "architecture" refers to the overall design of the network:
- How many layers
- How many neurons per layer
- What activation functions to use
- How layers are connected

There is no single right answer. Architecture is chosen based on the problem, the data, and experimentation.

**Shallow network:** One or two hidden layers. Works well for structured tabular data (spreadsheet-style data like house prices or customer records).

**Deep network:** Many hidden layers (3 or more). Needed for complex data like images, audio, and text. More depth allows the network to learn increasingly abstract representations.

**Wide network:** Many neurons per layer. More capacity per layer.

In practice, you start with a reasonable architecture and adjust based on whether the model is underfitting or overfitting.

---

## Quick Concept Summary

| Term | What It Means |
|------|--------------|
| Neuron | A single computing unit: weighted sum plus activation |
| Weight | Learnable parameter scaling each input connection |
| Bias | Learnable offset allowing the neuron to shift its output |
| Activation function | Non-linear function applied after the weighted sum |
| Input layer | Holds raw input features, no computation |
| Hidden layer | Intermediate layers that learn internal representations |
| Output layer | Produces the final prediction |
| Forward propagation | Passing input through layers to get a prediction |
| Backpropagation | Propagating error backwards to compute gradients |
| Epoch | One full pass through the training dataset |
| Batch | A subset of data used for one gradient update |
| Inference | Using a trained model to predict on new data |
| Architecture | The overall design: number of layers, neurons, activations |
