#%%

import numpy as np
import matplotlib.pyplot as plt

P = 400 #power of the car
m = 70 #mass of the bicycle 
v = 4 #Initial spped
h = 1.5 #height of person on the bike
s = 1000 #steps
eta = 2*10**(-5) #viscosity
A = 0.33
C = 1
rho_air = 1.27
rho_water = 1000
tmin = 0
tmax = 20
t = np.linspace(tmin, tmax, s)
dt = (tmax - tmin)/s

def v_num(x):
    return x + (P / (m*x))*dt - (C*rho_water*A*x**2)/(2*m)*dt - (eta*A*x/1.5)/m*dt

v_list = []

for i in t:
    v_list.append(v)
    v = v_num(v)

plt.plot(t, v_list)
plt.show()
