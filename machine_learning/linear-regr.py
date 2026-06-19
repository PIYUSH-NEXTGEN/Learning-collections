'''
Linear Regression learns the best-fitting straight-line relationship between input features and a continuous numerical target
by minimizing prediction error using a cost function and gradient descent.
'''
import numpy as np
import  matplotlib.pyplot as plt


x_train = np.array([1,2])     # x_train is the input variable
y_train = np.array([300,500]) # y_train is output variable
m = x_train.shape[0]          # m is the number of training examples
i = 0                         # i is the index for the  training example

x_i = x_train[i]
y_i = y_train[i]

plt.scatter(x_train,y_train,marker='x',color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Training Data')

w,b = 200, 100

def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)
plt.plot(x_train, tmp_f_wb, color='blue',label='Prediction')

plt.show()

