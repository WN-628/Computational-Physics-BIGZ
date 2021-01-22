#%%
import numpy as np

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    x_arr = np.linspace(a, b, n)
    A = 0
    for x in x_arr:
        A += 2*f(x)
    A = A - f(a) - f(b)
    A = 1/2*h*A
    return A

print(trapezoidal(lambda x: x**3, 2, 4, 1000000))

# %%
