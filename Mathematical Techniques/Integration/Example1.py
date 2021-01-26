#%%
import numpy as np

def Simpson(f, a, b, n=1000):
    h = (b-a)/n
    k = 0.0
    x = a+h
    for i in range(1, int(n/2) + 1):
        k += 4*f(x)
        x += 2*h

    x = a+2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

print(Simpson(lambda z: np.exp(-(z/(1-z))**2)*1/(z-1)**2, 0, 0.9999, 1000000))

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    x_arr = np.linspace(a, b, n)
    A = 0
    for x in x_arr:
        A += 2*f(x)
    A = A - f(a) - f(b)
    A = 1/2*h*A
    return A

print(trapezoidal(lambda z: np.exp(-(z/(1-z))**2)*1/(z-1)**2, 0, 0.9999, 1000000))