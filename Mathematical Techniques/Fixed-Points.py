from vpython.vpython import pyramid


import numpy as np

g = lambda x : 2 - np.exp(-x)
y = lambda x : np.exp(1 - x**2)
def accFunction(g, x0, Nmax, accuracy):
    n = 1
    x_current = x0
    acc = 100
    while n < Nmax and acc > accuracy:
        x = g(x_current)
        acc = np.abs(x_current - x)
        x_current = x
        n += 1
    if acc > accuracy:
        print("The function may not be diverged. ")
    else:
        print("The root of this function is ", x_current, ". \nThe accuracy is ", acc)

accFunction(y, 10, 500000, 10**(-6))