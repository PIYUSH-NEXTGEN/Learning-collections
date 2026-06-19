# Cost Function in Machine Learning

## What is a Cost Function?

A **cost function** is a mathematical function that measures how wrong a machine learning model's predictions are.

* Low Cost → Good predictions
* High Cost → Poor predictions

The goal of training is to **minimize the cost**.

---

## Why Do We Need It?

The model needs a way to know:

* How far it is from the correct answer
* Whether it is improving
* How to adjust its parameters

The cost function provides this feedback.

---

## Example

Suppose the actual house price is:

```text
Actual Price = 300
```

The model predicts:

```text
Predicted Price = 250
```

Error:

```text
300 - 250 = 50
```

The cost function converts these errors into a single number representing the model's overall performance.

---

## Mean Squared Error (MSE)

For Linear Regression, the most common cost function is:


$J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(\hat{y}_i-y_i)^2$


Where:

- $m$ = number of training examples
- $\hat{y}_i$ = predicted value for the $i^{th}$ training example
- $y_i$ = actual value for the $i^{th}$ training example
- $J(w,b)$ = cost function value
[

---

## Why Square the Error?

Consider:

```text
Error A = +10
Error B = -10
```

Adding them gives:

```text
10 + (-10) = 0
```

This incorrectly suggests no error.

Squaring solves the problem:

```text
10² = 100
(-10)² = 100
```

Benefits:

* Prevents positive and negative errors from cancelling out
* Penalizes larger errors more heavily

---

## How Training Uses Cost Function

Training follows this cycle:

```text
Make Prediction
       ↓
Calculate Cost
       ↓
Adjust Parameters
       ↓
Reduce Cost
       ↓
Repeat
```

The model continuously updates its parameters until the cost becomes as small as possible.

---

## Cost Function and Gradient Descent

Think of the cost function as a landscape:

```text
High Cost  = Top of Mountain
Low Cost   = Bottom of Valley
```

Gradient Descent is the algorithm that moves the model downhill toward the lowest cost.

```text
Cost Function → Defines the landscape
Gradient Descent → Finds the lowest point
```

---

## Loss Function vs Cost Function

### Loss Function

Error for a single training example.

Example:

```text
Actual = 300
Predicted = 250

Loss = (300 - 250)² = 2500
```

### Cost Function

Average loss across the entire dataset.

```text
Cost = Average of all losses
```

---

## Common Cost Functions

### Linear Regression

* Mean Squared Error (MSE)

### Binary Classification

* Binary Cross Entropy

### Multi-Class Classification

* Categorical Cross Entropy

---
