import matplotlib.pyplot as plt
import numpy as np

# DATASET 1
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost = 0

    for i in range(m):
        f_wb = w*x[i] + b
        cost += (f_wb - y[i]) ** 2

    total_cost = cost/(2*m)
    return cost

def compute_gradients(x,y,w,b):
    m = x.shape[0]

    dj_db = 0
    dj_dw = 0

    for i in range(m):
        f_wb = w * x[i] + b
        d_dw_i = (f_wb - y[i]) * x[i]
        d_db_i = f_wb - y[i]

        dj_dw += d_dw_i
        dj_db += d_db_i

    dj_db /= m
    dj_dw /= m

    return dj_db,dj_dw

def compute_gradient(x,y,w,b,cost_func,gradient_func,num_of_iters,alpha):

    j_hist = []
    p_hist = []
    w_ = w
    b_ = b

    for i in range(num_of_iters):
        dj_dw, dj_db = gradient_func(x, y, w, b)

        w_ = w - alpha(dj_dw)
        b_ = b - alpha(dj_db)

        if num_of_iters < 10000:
            j_hist.append(cost_func(x,y,w,b))
            p_hist.append([w,b])









