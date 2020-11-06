# %%
import numpy as np
import matplotlib.pyplot as plt

m = 80
f = 400
rho = 1.293
a = 0.45
cd = 1.2
w = 1
tc = 0.67
fc = 488
fv = 25.8
t_max = 10
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
a_arr = np.zeros(steps)
x_arr = np.zeros(steps)
v_arr = np.zeros(steps)

def A(t):
    return a*(1 - 0.25*np.exp(-(t/tc)**2))

def D(t, v):
    return 1/2*A(t)*rho*cd*(v - w)**2

def Fc(t):
    return fc*np.exp(-(t/tc)**2)

def Fv(v):
    return fv*v

def Ft(v, t):
    return (f + Fc(t) - Fv(v) - D(t, v)) / m

def next_v(v, t):
    return v + Ft(v, t)*dt

def next_x(v, x):
    return x + v*dt


for i in range(1, steps):
    a_arr[i] = Ft(v_arr[i - 1], t_arr[i - 1])
    v_arr[i] = next_v(v_arr[i - 1], t_arr[i - 1])
    x_arr[i] = next_x(v_arr[i], x_arr[i - 1])

# plt.plot(t_arr, v_arr)
plt.plot(t_arr, a_arr)
plt.legend(["a vs t"])
plt.subplots()
plt.plot(t_arr, v_arr)
plt.legend(["v vs t"])
plt.subplots()
plt.plot(t_arr, x_arr)
plt.legend(["x vs t"])
plt.show()


def find_x_index(x, arr):
    for i in range(len(arr)):
        if (arr[i] > x):
            return i


print("It takes ", t_arr[find_x_index(100, x_arr)], "for the runner to run 100m. ")

max_velocity = np.max(v_arr)
print("The maximum velocity of the person is ", max_velocity)


# %%
