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

m = 1
kx = 1
ky = 1
L = 1
T_max = 500  #maximum time span
steps = 5000
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
vx_arr = np.zeros(steps)
vx_arr[0] = 10
x_arr = np.zeros(steps)
x_arr[0] = 10
vy_arr = np.zeros(steps)
vy_arr[0] = 10
y_arr = np.zeros(steps)
y_arr[0] = 0.5
r_arr = np.zeros(steps)

# for i in range(steps):
#     r_arr[i] = (x_arr[i]**2 + y_arr[i]**2)**(1/2)

# def next_v(x, y, v, k):
#     r = (x**2 + y**2)**(1/2)
#     return v - k/m*(r - L)*x/r*dt

# def next_x(v, x):
#     return x + v*dt

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
    r = ((x_arr[i - 1])**2 + (y_arr[i - 1])**2)**(1/2)
    vx_arr[i] = vx_arr[i - 1] - kx/m*(r - L)*x_arr[i - 1]/(r)*dt
    x_arr[i] = x_arr[i - 1] + vx_arr[i]*dt
    vy_arr[i] = vy_arr[i - 1] - ky/m*(r - L)*y_arr[i - 1]/(r)*dt
    y_arr[i] = y_arr[i - 1] + vy_arr[i]*dt

plt.plot(x_arr, y_arr)
plt.show()

import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-18, 18), ylim=(-18, 18)) # Set x and y limit. Change according to your graph. 
line, = ax.plot([], [], lw=3)
def init():
    line.set_data([], [])
    return line,
def animate(i):
    # Generates a graph for current i. Change x and y to your x and y data list. 
    _x = x_arr[:i] 
    _y = y_arr[:i]
    line.set_data(_x, _y) 
    return line,
# Change frame and interval according to your data. 
# frames should be the length of your data array. 
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=5000, interval=100, blit=True) 
anim.save('pic.gif', writer='imagemagick')
