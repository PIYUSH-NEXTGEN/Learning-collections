# Gradient Descent 
Gradient Descent is an optimization algorithm used to find the best values of model parameters (such as `w` and `b`) by minimizing the cost (error) function.

---

## Real-Life Analogy

Imagine standing on a mountain in the dark and trying to reach the lowest point.

1. Feel the slope beneath your feet.
2. Take a small step downhill.
3. Repeat until you reach the valley.

The valley represents the minimum cost.

---

## Why Do We Need It?

For Linear Regression:

[
f(x) = wx + b
]

We need to find the best values of:

* `w` (slope)
* `b` (intercept)

that minimize prediction error.

---

## Cost Function

The cost function measures how bad the predictions are:

[
$J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(f(x_i)-y_i)^2$
]

* High Cost → Poor predictions
* Low Cost → Better predictions
* Cost = 0 → Perfect predictions

---

## Main Idea

Gradient Descent repeatedly:

1. Makes predictions
2. Calculates errors
3. Computes gradients (slopes)
4. Updates parameters
5. Repeats until cost is minimized

---

## Gradient

A gradient tells us:

> Which direction increases the cost the fastest?

Since we want to decrease cost, we move in the opposite direction of the gradient.

---

## Update Rule

For parameter `w`:

[
$w = w - \alpha \frac{\partial J}{\partial w}$
]

For parameter `b`:

[
$b = b - \alpha \frac{\partial J}{\partial b}$
]

Where:

* `α` = Learning Rate
* `∂J/∂w` = Gradient with respect to `w`
* `∂J/∂b` = Gradient with respect to `b`

---

## Learning Rate (α)

Controls step size during optimization.

### Too Small

* Very slow learning
* Takes many iterations

### Too Large

* Overshoots the minimum
* May never converge

### Good Learning Rate

* Reaches minimum efficiently
* Stable convergence

Common values:

```python
0.1
0.01
0.001
```

---

## Linear Regression Gradients

For:

[
f(x)=wx+b
]

Gradient for `w`:

[
$\frac{\partial J}{\partial w}$
=============================

$\frac{1}{m}
\sum_{i=1}^{m}
(f(x_i)-y_i)x_i$
]

Gradient for `b`:

[
$\frac{\partial J}{\partial b}$
=============================

$\frac{1}{m}
\sum_{i=1}^{m}
(f(x_i)-y_i)$
]
---
# Mathematical Example of Gradient Descent

## Problem

Suppose we want to minimize the function:

[
J(w) = w^2
]

The minimum value occurs at:

[
w = 0
]

Let's see how Gradient Descent finds it.

---

## Step 1: Find the Gradient

Differentiate the cost function:

[
$J(w)=w^2$
]

[
$\frac{dJ}{dw}=2w$
]

This tells us the slope at any value of (w).

---

## Step 2: Choose Initial Values

Let's start with:

```text
w = 4
Learning Rate (α) = 0.1
```

---

## Step 3: Apply Gradient Descent

Update Rule:

[
$w = w - \alpha \frac{dJ}{dw}$
]

Substitute values:

[
$w = 4 - 0.1(2 \times 4)$
]

[
w = 4 - 0.8
]

[
w = 3.2
]

---

## Iteration 2

Current:

[
w = 3.2
]

Gradient:

[
2w = 6.4
]

Update:

[
w = 3.2 - 0.1(6.4)
]

[
w = 2.56
]

---

## Iteration 3

Current:

[
w = 2.56
]

Gradient:

[
2w = 5.12
]

Update:

[
w = 2.56 - 0.1(5.12)
]

[
w = 2.048
]

---

## Progress Table

| Iteration | w      |
| --------- | ------ |
| 0         | 4.0000 |
| 1         | 3.2000 |
| 2         | 2.5600 |
| 3         | 2.0480 |
| 4         | 1.6384 |
| 5         | 1.3107 |
| 10        | 0.4295 |
| 20        | 0.0461 |

---

## Observation

Notice that:

* (w) gets smaller every iteration.
* The updates become smaller as we approach the minimum.
* Eventually:

[
$w \rightarrow 0$
]

which is exactly the minimum of:

[
$J(w)=w^2$
]

---

## Types of Gradient Descent

### 1. Batch Gradient Descent

Uses the entire dataset before updating parameters.

* Accurate
* Slow on large datasets

### 2. Stochastic Gradient Descent (SGD)

Updates after every training example.

* Fast
* Noisy updates

### 3. Mini-Batch Gradient Descent

Updates after small batches (32, 64, 128 samples, etc.).

* Fast
* Stable
* Most commonly used in Deep Learning

---


---

## Key Takeaway

Gradient Descent is the foundation of:

* Linear Regression
* Logistic Regression
* Neural Networks
* Deep Learning
* Large Language Models (LLMs)
