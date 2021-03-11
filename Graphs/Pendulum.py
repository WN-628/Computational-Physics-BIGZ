#%%
# from numpy import *
import numpy as np
from vpython import *

# http://techforcurious.website/simulation-of-pendulum-vpython-tutorial-visual-python/

# Initialize the objects
canvas(width = 1280, height = 720)
# canvas(width = 3840, height = 2160)
bob = sphere(pos = vector(5, 2, 0), radius = 0.5)
pivot = vector(0, 20, 0)
Ceiling = box(pos = pivot, size = vector(10, 0.5, 10), color = color.green)
rod = helix(pos = pivot, axis = bob.pos-pivot, radius = 0.5, coils = 10)

# Constant
m = 1
g = 9.8 
L = mag(bob.pos - pivot) #length of pendulum
cs = (pivot.y - bob.pos.y)/L #Calculation of cos(theta)
theta = acos(cs) #angle wih vertical direction
angvel = 0.0 #angular velocity
k = 20 #Spring constant
v_x = 0
v_y = 0

# Initialize the time
tmin = 0
tmax = 500
step = 100000
dt = (tmax - tmin)/step

t = 0

while(t < tmax):
    # Fel = k*(((L*sin(theta))**2 + (pivot.y - L*cos(theta))**2) - L) #Elastic force of the spring
    # Fel = k*(((L*sin(theta))**2 + (L*cos(theta))**2)**(1/2) - L)
    Fel = k*(np.sqrt((L*sin(theta))**2 + (L*cos(theta))**2) - L)
    acc_x = Fel*sin(theta)/m
    v_x += acc_x*dt
    acc_y = (- m*g - Fel*cos(theta))/m
    v_y += acc_y*dt
    rate(500) #maximum 100 calculations per second
    acc = -g/L*sin(theta) #updating of auglar acceleration
    theta = theta + angvel*dt #updating of angular position
    angvel = angvel + acc*dt #updating of angular velocity
    bob.pos = vector(L*sin(theta) + v_x*dt, pivot.y - L*cos(theta) + v_y*dt, 0) #cal. postition
    rod.axis = bob.pos - rod.pos #updating other end of rod of pendulum 
    t = t + dt # updating time

# while(t < tmax):
    
# %%
