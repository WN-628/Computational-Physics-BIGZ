#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

f = lambda x : 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

t_arr = np.linspace(0.0, 1.0, 1000)
f_arr = []

for t in t_arr:
    f_arr.append(f(t))

plt.plot(t_arr, f_arr)
plt.show()