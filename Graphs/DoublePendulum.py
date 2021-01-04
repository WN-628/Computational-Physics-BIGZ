import numpy as np
from scipy.integrate import solve_ivp 
from vpython import *

m1 = 10
m2 = 10
l1 = 5
l2 = 5
g = 9.8


# y = np.array([theta1, theta2, omega1, omega2])
def f(x, y):
    a = x[0]
    b = y[0]
    w1 = x[1]
    w2 = y[1]
    f_1 = l1 / l2 * w1**2 * np.sin(a - b) - l1 / l2 * x[1] * np.cos(a - b) - g / l1 * np.sin(b)
    f_2 = (m2 * l2 * w2**2 * np.sin(a - b) + (m1 + m2) * g * np.sin(a) + m2 * l2 *np.cos(a - b) * (l1 / l2 * w1**2 * np.sin(a - b) - g / l1 * np.sin(b))) / (m2 * l1 * (np.cos(a - b))**2 - (m1 + m2) * l1)
    return np.array([w1, w2, f_1, f_2])

Y0 = np.array([0,0,0,0]) 
sol = solve_ivp(f, [0,10], Y0, method='Radau', dense_output=True)

t = np.linspace(0, 10, 1001) 
Y = sol.sol(t) 

plt.plot(t, Y[1],'-', label='r(t)') 
plt.plot(t, Y[2],'-', label='phi(t)')
plt.legend(loc='best')
plt.xlabel('T')
