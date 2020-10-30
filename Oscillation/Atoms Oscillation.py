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
import numpy as np
import matplotlib.pyplot as plt

m = 5
kx = 1
ky = 10
L = 10
T_max = 5000  #maximum time span
steps = 10000
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
vx_arr = np.zeros(steps)
vx_arr[0] = 2
x_arr = np.zeros(steps)
x_arr[0] = 5
vy_arr = np.zeros(steps)
vy_arr[0] = 2
y_arr = np.zeros(steps)
y_arr[0] = 5
r_arr = np.zeros(steps)

# for i in range(steps):
#     r_arr[i] = (x_arr[i]**2 + y_arr[i]**2)**(1/2)

def next_v(x, y, v, k):
    r = (x**2 + y**2)**(1/2)
    return v - k/m*(r - L)*x/r*dt

def next_x(v, x):
    return x + v*dt

# for i in range(0, interval, 1):
#     vx[i+1] = vx[i] + (- k * ((x[i]**2 + y[i]**2) ** (1/2) - L0) * x[i] / ((x[i]**2 + y[i]**2) ** (1/2))) * dt
#     x[i+1] = x[i] + vx[i+1] * dt
#     vy[i+1] = vy[i] + (- k * ((x[i]**2 + y[i]**2) ** (1/2) - L0) * y[i] / ((x[i]**2 + y[i]**2) ** (1/2))) * dt
#     y[i+1] = y[i] + vy[i+1] * dt

# for i in range(1, steps):
#     vx_arr[i] = next_v(x_arr[i - 1], y_arr[i - 1], vx_arr[i - 1], kx)
#     x_arr[i] = next_x(x_arr[i - 1], vx_arr[i])
#     vy_arr[i] = next_v(y_arr[i - 1], x_arr[i - 1], vy_arr[i - 1], ky)
#     t_arr[i] = next_x(y_arr[i - 1], vy_arr[i])

for i in range(1, steps):
    vx_arr[i] = vx_arr[i - 1] + (- kx/m * ((x_arr[i - 1]**2 + y_arr[i - 1]**2) ** (1/2) - L) * x_arr[i - 1] / ((x_arr[i - 1]**2 + y_arr[i - 1]**2) ** (1/2))) * dt
    x_arr[i] = next_x(x_arr[i - 1], vx_arr[i])
    vy_arr[i] = vy_arr[i - 1] + (- ky/m * ((x_arr[i - 1]**2 + y_arr[i - 1]**2) ** (1/2) - L) * y_arr[i - 1] / ((x_arr[i- 1]**2 + y_arr[i - 1]**2) ** (1/2))) * dt
    t_arr[i] = next_x(y_arr[i - 1], vy_arr[i])

plt.plot(x_arr, y_arr)
plt.show()
# %%
