#%%
# Relaxation-method
import numpy as np
import matplotlib.pyplot as plt

theta0 = np.pi/4
v0 = 30
g = 9.8
x = 90
y = 1
y0 = 1.8

f = lambda theta : (np.tan(theta)*x - g/(2*v0**2*np.cos(theta)**2)*x**2 + y0 - y)

def accFunction(f, theta0, Nmax, accuracy):
    n = 1
    theta_current = theta0
    acc = 100
    while n < Nmax and acc > accuracy:
        theta = f(theta_current)
        acc = np.abs(theta_current - theta)
        theta_current = theta
        n += 1
    if acc > accuracy:
        print("The function may be diverged. ")
    else:
        print("The root of this function is ", theta_current, "\nThe accuracy is ", acc)
    return theta_current

accFunction(f, theta0, 500000, 10**(-6))

c_arr = np.linspace(0, 3, 10000)
theta_arr = []

for c in c_arr:
    theta_arr.append(accFunction(f, theta0, 500000, 10**(-6)))

plt.plot(c_arr, theta_arr)
plt.show()