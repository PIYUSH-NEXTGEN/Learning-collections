# Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict a **continuous numerical value** by finding the best-fitting straight line through the data.

Examples:

* House price prediction
* Salary prediction
* Sales forecasting
* Temperature prediction

---

## Linear Regression Equation

$$
\hat{y} = wx + b
$$

Where:

* $x$ = input feature
* $\hat{y}$ = predicted output
* $w$ = weight (slope)
* $b$ = bias (intercept)

---

## Goal

Find the optimal values of **weight (w)** and **bias (b)** so that predictions are as close as possible to actual values.


## Cost Function

Linear Regression uses **Mean Squared Error (MSE)** to measure prediction error.

$$
J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(\hat{y}_i-y_i)^2
$$

Where:

* $m$ = number of training examples
* $\hat{y}_i$ = predicted value
* $y_i$ = actual value

### Purpose

* High Cost → Poor predictions
* Low Cost → Better predictions

---

## Gradient Descent

Gradient Descent is used to minimize the cost function.

Process:

```text
Make Predictions
       ↓
Calculate Cost
       ↓
Update w and b
       ↓
Reduce Error
       ↓
Repeat
```

---

## Types

### Simple Linear Regression

One input feature:

$$
\hat{y}=wx+b
$$

### Multiple Linear Regression

Multiple input features:

$$
\hat{y}=w_1x_1+w_2x_2+\cdots+w_nx_n+b
$$

---

## When to Use

* Target variable is numerical
* Relationship is approximately linear
* Model interpretability is important

---

## Training Flow

```text
Training Data
      ↓
Initialize w and b
      ↓
Make Predictions
      ↓
Calculate Cost (MSE)
      ↓
Gradient Descent
      ↓
Update Parameters
      ↓
Repeat Until Cost is Minimum
```

---
