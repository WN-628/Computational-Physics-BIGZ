#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x = sym.symbols('x')
f = 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
g = sym.diff(f)

t_arr = np.linspace(0.0, 1.0, 1000)
f_arr = []

for t in t_arr:
    f_arr.append(np.float(g.evalf(subs = {x : t})))

plt.plot(t_arr, f_arr)
plt.show()

def NewtonRaphson(f, g, x0, Nmax, accuracy):
    n = 1
    x_current = x0
    acc = 100
    x = x0
    while n < Nmax and acc > accuracy:
        x = x_current - np.float(f.evalf(subs = {x : x_current})) / np.float(g.evalf(subs = {x : x_current}))
        acc = abs(x_current - x)
        x_current = x
        n += 1
        print(x, acc, x_current, n)
    if acc > accuracy:
        print("The function may be diverged. ")
    else:
        print("The root of this function is ", x_current, "\nThe accuracy is ", acc)
    return x_current

NewtonRaphson(f, g, 10, 5, 10**(-10))
# %%
