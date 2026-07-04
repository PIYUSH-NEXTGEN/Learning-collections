import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import  PolynomialFeatures

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 5, 10, 17, 26,])

poly  = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

print(x_poly)

model = LinearRegression()
model.fit(x_poly,y)


print(model.coef_)
print(model.intercept_)



