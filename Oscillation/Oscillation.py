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
b = 0.1  #Drag constant
k = 10  #spring constant
O = (k/m)**(1/2)  #Natural frequency of the system
F0 = 5 #External Force
n = 50  #How many periods
P = 2*np.pi*(m/k)**(1/2)  #Periods
T_max = n*P  #maximum time span
steps = 1000  
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 10

def next_v(v, x, t, a):
    return v + (- k*x - b*v + F0*np.sin(a*O*t))/m*dt

def next_x(v, x):
    return x + v*dt

for Omega in [0.001, 0.1, 1, 10, 1000]:
    for i in range(1, steps):
        v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1], t_arr[i], Omega)
        x_arr[i] = next_x(v_arr[i], x_arr[i - 1])
    plt.plot(t_arr, x_arr)
plt.legend(["Omega = 0.001", "Omega = 0.1", "Omega = 1", "Omega = 10", "Omega = 1000"])
plt.show()

# %%
m = 1
L = 10
g = 9.8
T_max = 50  #maximum time span
steps = 1000
dt = T_max / steps  #Discretize time

t_arr = np.linspace(0, T_max, steps)
Theta_arr = np.zeros(steps)
Theta_arr[0] = 36*2*np.pi/360
O_arr = np.zeros(steps)
O_arr[0] = 0

def next_Omega(theta, Omega):
    return Omega - g/L*np.sin(theta)*dt 

def next_theta(theta, Omega):
    return theta + Omega*dt

for i in range(1, steps):
    O_arr[i] = next_Omega(Theta_arr[i - 1], O_arr[i - 1])
    Theta_arr[i] = next_theta(Theta_arr[i - 1], O_arr[i])
# plt.plot(t_arr, Theta_arr)
# # plt.plot(t_arr, O_arr)
# plt.show()

# %%
def findzeros(a_arr, start):
    for i in range(start, len(a_arr)):
        if (a_arr[i] > 0 and a_arr[i + 1] < 0) or (a_arr[i] < 0 and a_arr[i + 1] > 0):
            return i + 1

def findperiod(arr):
    t1index = findzeros(arr, 0)
    t2index = findzeros(arr, t1index)
    return [t1index, t2index]

index = findperiod(Theta_arr)
period = (((t_arr[index[1]] + t_arr[index[1] - 1])/2) - ((t_arr[index[0]] + t_arr[index[0] - 1])/2))*2
print("The period of this motion is ", period)
plt.plot(t_arr, Theta_arr)
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

m = 1
L = 10
g = 9.8
T_max = 50  #maximum time span
stepsT = 1000
dt = T_max / stepsT  #Discretize time
theta_min = 1
theta_max = 89
steps = 20
theta0_arr = np.linspace(theta_min, theta_max, steps)
period_arr = np.zeros(steps)

def findzeros(a_arr, start):
    for i in range(start + 1, len(a_arr)):
        if (a_arr[i - 1] > 0 and a_arr[i] < 0) or (a_arr[i - 1] < 0 and a_arr[i] > 0):
            return i

def findperiod(arr):
    t1index = findzeros(arr, 0)
    t2index = findzeros(arr, t1index)
    return [t1index, t2index]

for i in theta0_arr:
    t_arr = np.linspace(0, T_max, stepsT)
    Theta_arr = np.zeros(stepsT)
    Theta_arr[0] = i*2*np.pi/360
    O_arr = np.zeros(steps)
    O_arr[0] = 0
    def next_Omega(theta, Omega):
        return Omega - g/L*np.sin(theta)*dt 

    def next_theta(theta, Omega):
        return theta + Omega*dt

    for i in range(1, steps):
        O_arr[i] = next_Omega(Theta_arr[i - 1], O_arr[i - 1])
        Theta_arr[i] = next_theta(Theta_arr[i - 1], O_arr[i])
    index = findperiod(Theta_arr)
    period_arr[i] = (((t_arr[index[1]] + t_arr[index[1] - 1])/2) - ((t_arr[index[0]] + t_arr[index[0] - 1])/2))*2

plt.plot(theta0_arr, period_arr)
plt.show()
    
# %%
