# %%
# Lattice Spring Model
import numpy as np
import matplotlib.pyplot as plt

m = 5
kx = 1
ky = 10
T_max = 50  #maximum time span
steps = 1000
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
vx_arr = np.zeros(steps)
vx_arr[0] = 0
x_arr = np.zeros(steps)
x_arr[0] = 5
vy_arr = np.zeros(steps)
vy_arr[0] = 0
y_arr = np.zeros(steps)
y_arr[0] = 5

def next_vx(x, vx):
    return vx - 2*kx/m*x*dt

def next_x(x, vx):
    return x + vx*dt

def next_vy(y, vy):
    return vy - 2*ky/m*y*dt

def next_y(y, vy):
    return y + vy*dt

for i in range(1, steps):
    vx_arr[i] = next_vx(x_arr[i - 1], vx_arr[i - 1])
    x_arr[i] = next_x(x_arr[i - 1], vx_arr[i])
    vy_arr[i] = next_vy(y_arr[i - 1], vy_arr[i - 1])
    y_arr[i] = next_y(y_arr[i - 1], vy_arr[i])
plt.plot(x_arr, y_arr)
plt.show()

# %%
# Full Spring Model