#%%
import numpy as np
import matplotlib.pyplot as plt

c = 2
g = lambda x : 1 - np.exp(-c*x)
def accFunction(g, x0, Nmax, accuracy):
    n = 1
    x_current = x0
    acc = 100
    while n < Nmax and acc > accuracy:
        x = g(x_current)
        acc = np.abs(x_current - x)
        x_current = x
        n += 1
    # if acc > accuracy:
    #     print("The function may not be diverged. ")
    # else:
    #     print("The root of this function is ", x_current, "\nThe accuracy is ", acc)
    return x_current

accFunction(g, 10, 500000, 10**(-6))

c_arr = np.linspace(0, 3, 10000)
x_arr = []

for c in c_arr:
    x_arr.append(accFunction(g, 10, 500000, 10**(-6)))

plt.plot(c_arr, x_arr)
plt.show()

