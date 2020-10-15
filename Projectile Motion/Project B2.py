# %%

import numpy as np
import matplotlib.pyplot as plt
import math as math

v0 = 700
# b/m = 4*10**(-5)
g = 9.8
theta = np.pi/6
t_min = 0
t_max = 2*(v0*math.sin(theta) / g)
step = 1000
Me = 5.972*10**24
G = 6.674*10**-8
h_min = 0
h_max = 1000
R = 6.371*10**6

# Use Euler Method to plot a projectile with not air drag
t_arr = np.linspace(t_min, t_max, 1000)
dt = t_max/step
x = np.zeros(len(t_arr))
x_val = 0
y = np.zeros(len(t_arr))
y_val = 0
vx = np.zeros(len(t_arr))
vx_val = v0*math.cos(theta)
vy = np.zeros(len(t_arr))
vy_val = v0*math.sin(theta)


# # Plot the true value of the projectile motion
x_true = np.zeros(len(t_arr))
# x_true_val = 0
vx_true = v0*math.cos(theta)
y_true = np.zeros(len(t_arr))
# y_true_val = 0
# vy_true = v0*math.sin(theta) - g*dt


def dx_next(x, vx):
    return x + vx*dt


def dy_next(a, b):
    return a + b*dt


def Grav(G, M, y):
    return G*M/(y + R)**2


def vy_next(vy, y_val):
    return vy - Grav(G, Me, y_val)*dt


for i in range(len(t_arr)):
    vx[i] = vx_val
    vy[i] = vy_val
    x[i] = x_val
    y[i] = y_val
    x_val = dx_next(x_val, vx_val)
    y_val = dy_next(y_val, vy_val)
    vy_val = vy_next(vy_val, y_val)

# plt.plot(x, y)
# plt.show()

# for i in range(len(t_arr)):
#     _t = t_arr[i]
#     x_true[i] = vx_true*_t
#     y_true[i] = v0*math.sin(theta)*_t - 1/2*g*_t**2

plt.plot(x, y)
plt.title("Projectile Motion with varing g")
plt.show()


# %%
