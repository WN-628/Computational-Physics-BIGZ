#%%
import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 10
n = 10
P = 2*np.pi*(m/k)**(1/2)
T_max = n*P
steps = 1000
dt = T_max / steps

t_arr = np.linspace(0, T_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 10

def next_v(v, x):
    return v + (-k*x)*dt

def next_x(v, x):
    return x + v*dt

for i in range(1, steps):
    v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
    x_arr[i] = next_x(v_arr[i - 1], x_arr[i -1])

plt.plot(t_arr, x_arr)
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 10
n = 10
P = 2*np.pi*(m/k)**(1/2)
T_max = n*P
steps = 1000
dt = T_max / steps

t_arr = np.linspace(0, T_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 10

def next_v(v, x):
    return v + (-k*x)*dt

def next_x(v, x):
    return x + v*dt

for i in range(1, steps):
    v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
    x_arr[i] = next_x(v_arr[i], x_arr[i - 1])

plt.plot(t_arr, x_arr)
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

# a = 3   ##alpha for simple harmonic motion
m = 1   ##mass of the block
k = 10  #spring constant
n = 5  #How many periods
P = 2*np.pi*(m/k)**(1/2)  #Periods
T_max = n*P  #maximum time span
steps = 1000  
dt = T_max / steps  #Discretize time

for a in [1, 3]:
    t_arr = np.linspace(0, T_max, steps)
    x_arr = np.zeros(steps)
    x_arr[0] = 0
    v_arr = np.zeros(steps)
    v_arr[0] = 10

    def next_v(v, x):
        return v + (-k*x**a)*dt

    def next_x(v, x):
        return x + v*dt

    for i in range(1, steps):
        v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
        x_arr[i] = next_x(v_arr[i], x_arr[i - 1])

    plt.plot(t_arr, x_arr)
plt.legend(["a=1", "a=3"])
plt.show()

# %%
m = 1   ##mass of the block
b = 10
k = 10  #spring constant
n = 10  #How many periods
P = 2*np.pi*(m/k)**(1/2)  #Periods
T_max = n*P  #maximum time span
steps = 1000  
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 10

def next_v(v, x):
    return v + (- k*x - b*v)/m*dt

def next_x(v, x):
    return x + v*dt

for b in [0, 1, 5, 10, 100]:
    for i in range(1, steps):
        v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
        x_arr[i] = next_x(v_arr[i], x_arr[i - 1])
    plt.plot(t_arr, x_arr)
plt.legend(["b = 0", "b = 1", "b = 5", "b = 10", "b = 100"])
plt.show()

# %%
m = 1   ##mass of the block
b = 10  #Drag constant
k = 10  #spring constant
O = (k/m)**(1/2)  #Natural frequency of the system
F0 = 10 #External Force
n = 10  #How many periods
P = 2*np.pi*(m/k)**(1/2)  #Periods
T_max = n*P  #maximum time span
steps = 1000  
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 10

def next_v(v, x, t):
    return v + (- k*x - b*v + F0*np.sin())/m*dt

def next_x(v, x):
    return x + v*dt

for i in range(1, steps):
    v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
    x_arr[i] = next_x(v_arr[i], x_arr[i - 1])
plt.plot(t_arr, x_arr)
plt.legend([])
plt.show()