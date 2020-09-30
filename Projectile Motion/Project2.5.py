import numpy as np
import matplotlib.pyplot as plt

P = 400 #power of the car
m = 70 #mass of the bicycle 
v = 4 #Initial spped
h = 1.5 #height of person on the bike
s = 1000 #steps
g = 9.8 #gravitational constant
h = 1.5 #the height of bicycle and the person
eta_air = 2*10**(-5) #viscosity for air
eta_water = 10**(-3) #viscosity for water
A = 0.01 #Area
C = 1
rho_air = 1.27 #Density of air
rho_water = 1000 #Density of water
ttheta = 0.1 #the value of tangent
v0 = 7
F0 = P/v0
tmin = 0
tmax = 20
t = np.linspace(tmin, tmax, s)
dt = (tmax - tmin)/s

def v_num1(x):
    return x + F0/m*dt

def v_num(x):
    return x + (P / (m*x))*dt - (C*rho_air*A*x**2)/(2*m)*dt - (eta_air*A*x/h)/m*dt - g*np.sin(np.arctan(ttheta))*dt

v_list = []

for i in t:
    v_list.append(v)
    v = v_num(v)

plt.plot(t, v_list)
plt.show()
