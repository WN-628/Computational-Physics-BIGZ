#%%
import numpy as np
import matplotlib.pyplot as plt

m = 80
F = 400
rho = 1.293
Cd = 1.2
A = 0.45
w = 0
t_max = 50
steps = 1000
dt = t_max / steps

t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
x_arr[0] = 0
v_arr = np.zeros(steps)
v_arr[0] = 0

def next_v(v, x):
    return v + ((F - (1/2)*rho*Cd*A*(v - w)**2) / m)*dt

def next_x(v, x):
    return x + v*dt

for i in range(1, steps):
    v_arr[i] = next_v(v_arr[i - 1], x_arr[i - 1])
    x_arr[i] = next_x(v_arr[i], x_arr[i - 1])

# plt.plot(t_arr, v_arr)
plt.plot(t_arr, x_arr)
plt.show()

def find_x_index(x, arr):
    for i in range(len(arr)):
        if (arr[i] > x):
            return i

print("It takes ", t_arr[find_x_index(100, x_arr)], "for the runner to run 100m. ")

max_velocity = np.max(v_arr)
print("The maximum velocity of the person is ", max_velocity)

