#%%
import numpy as np 
import matplotlib.pyplot as plt 

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

def graphE(e):
    omega = 2*np.pi
    a = 1 / (1 - e)
    b = np.sqrt((1 + e) / (1 - e))
    t_arr = np.linspace(0, 1, 1000)
    x_arr = np.zeros(1000)
    y_arr = np.zeros(1000)
    for i in range(1000):
        E = accFunction(lambda E : omega*t_arr[i] + e*np.sin(E), 0, 100000, 10**(-6))
        x_arr[i] = a*(e - np.cos(E))
        y_arr[i] = b*np.sin(E)
    plt.plot(x_arr, y_arr)

for e in [0, 1/4, 1/2, 3/4]:
    graphE(e)

plt.axis("equal")
plt.show()