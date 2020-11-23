#%%
from numpy import *
from vpython import *

# http://techforcurious.website/simulation-of-pendulum-vpython-tutorial-visual-python/

# Initialize the objects
bob = sphere(pos = vector(5, 2, 0), radius = 0.5)
pivot = vector(0, 20, 0)
Ceiling = box(pos = pivot, size = vector(10, 0.5, 10), color = color.green)
rod = helix(pos = pivot, axis = bob.pos-pivot, radius = 0.5)

# Constant
g = 9.8 
L = mag(bob.pos - pivot) #length of pendulum
cs = (pivot.y - bob.pos.y)/L #Calculation of cos(theta)
theta = acos(cs) #angle wih vertical direction
angvel = 0.0 #angular velocity

# Initialize the time
tmin = 0
tmax = 100
step = 10000
dt = (tmax - tmin)/step

t = 0

while(t < tmax):
    rate(100) #maximum 100 calculations per second
    acc = -g/L*sin(theta) #updatin of auglar acceleration
    theta = theta + angvel*dt #updating of angular position
    angvel = angvel + acc*dt #updating of angular velocity
    bob.pos = vector(L*sin(theta), pivot.y - L*cos(theta), 0) #cal. postition
    rod.axis = bob.pos - rod.pos #updating other end of rod of pendulum 
    t = t + dt # updating time