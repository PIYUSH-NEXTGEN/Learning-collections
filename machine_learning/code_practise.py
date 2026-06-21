import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i]) ** 2

    return cost / (2 * m)

def compute_gradients(x, y, w, b):
    m = x.shape[0]

    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b
        error = f_wb - y[i]

        dj_dw += error * x[i]
        dj_db += error

    dj_dw /= m
    dj_db /= m

    return dj_dw, dj_db

def gradient_descent(x, y, w, b, alpha, num_iters, cost_func, grad_func):

    J_history = []
    P_history = []

    for i in range(num_iters):

        dj_dw, dj_db = grad_func(x, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        J_history.append(cost_func(x, y, w, b))
        P_history.append([w, b])

        if i % max(1, num_iters // 10) == 0:
            print(
                f"Iter {i:5} | Cost {J_history[-1]:.4f} | "
                f"w {w:.4f} | b {b:.4f}"
            )

    return w, b, J_history, P_history

w_init = 0
b_init = 0
alpha = 0.1
num_iters = 100000

w_final, b_final, J_hist, P_hist = gradient_descent(
    x, y,
    w_init, b_init,
    alpha,
    num_iters,
    compute_cost,
    compute_gradients
)

print(f"\nFinal (w, b): ({w_final:.4f}, {b_final:.4f})")

y_pred = w_final * x + b_final

plt.scatter(x, y, color='red', label='Data')
plt.plot(x, y_pred, label='Fit')
plt.legend()
plt.show()

plt.plot(J_hist)
plt.title("Cost vs Iterations")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()












