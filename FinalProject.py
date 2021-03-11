#%%
# import package that is needed
import numpy as np
from vpython import *

# Constant
m = 10 #kg
g = 9.8 #m/s^2
L0 = 10 #initial length of the spring in meters
theta = np.pi/6 #initial angle
angvel = 0.0 #rad/s initial angular velocity
k = 5 #spring constant
v_x = 0
v_y = 0
L = (m*g*np.cos(theta))/k + L0
angularV = 0 #angular velocity in rad / sec

# Initialize the objects
canvas(width = 1280, height = 720)
# canvas(width = 3840, height = 2160)
pivot = vector(0, 20, 0)
bob = sphere(pos = vector(pivot.x + L*np.sin(theta), pivot.y - L*np.cos(theta), 0), radius = 0.5)
Ceiling = box(pos = pivot, size = vector(10, 0.5, 10), color = color.green)
rod = helix(pos = pivot, axis = bob.pos-pivot, radius = 0.5, coils = 30)
lengthDisp = wtext(text='{}'.format(L))

#Set up the time range
tmin = 0
tmax = 500
step = 1000000
dt = (tmax - tmin)/step

t = 0 #record the time

while(t < tmax):
    tor = m*g*sin(theta)*L
    angularAcc = tor / (m*L**2)
    angularV = angularV + angularAcc*dt
    theta = theta - angularV*dt
    rate(1500)
    L = (m*g*np.cos(theta))/k + L0
    bob.pos = vector(pivot.x + L*np.sin(theta), pivot.y - L*np.cos(theta) + v_y*dt, 0)
    rod.axis = bob.pos - rod.pos
    t = t + dt
    lengthDisp.text = '{}'.format(L)

# %%
