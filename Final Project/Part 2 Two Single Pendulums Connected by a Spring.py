#%%
# import package that is needed
import numpy as np
from vpython import *

# https://physicscatalyst.com/graduation/coupled-pendulums/

# Constant
m1 = 5 # Mass of the ball at the left (kg)
v1 = 0 # The speed of ball1 (m/s)
m2 = 5 # Mass of the ball at the right (kg)
v2 = 0 # The speed of ball2 (m/s)
Ls = 10 # Length of the string (m)
L0 = 10 # Original length of the spring (m)
L = L0 # Instant length of the spring(m)
k = 10 # Spring constant (kg / s^2)
g = 9.8 # Gravitational constant
theta1 = -np.pi/20 # The angle for the first ball
theta2 = np.pi/20 # The angle for the second ball

# Initialize the objects
canvas(width = 1280, height = 720) # For 1080p screen
# canvas(width = 3840, height = 2160) # For 4k screen
pivot = vector(0, 20, 0)
pivot1 = vector(-5, 20, 0)
pivot2 = vector(5, 20, 0)
bob1 = sphere(pos = vector(pivot1.x + Ls*np.sin(theta1), pivot1.y - Ls*np.cos(theta1), 0), radius = 0.5)
string1 = cylinder(pos = pivot1, axis = bob1.pos - pivot1, radius = 0.05)
bob2 = sphere(pos = vector(pivot2.x + Ls*np.sin(theta2), pivot2.y - Ls*np.cos(theta2), 0), radius = 0.5)
string2 = cylinder(pos = pivot2, axis = bob2.pos - pivot2, radius = 0.05)
Ceiling = box(pos = pivot, size = vector(20, 0.5, 20), color = color.green)
spring = helix(pos = bob1.pos, axis = bob2.pos - bob1.pos, radius = 0.3, coils = 20)
L = ((bob2.pos.x - bob1.pos.x)**2 + (bob2.pos.y - bob1.pos.y)**2)
a = wtext(text='length of the spring: {} m \n'.format(L))
b = wtext(text='pos of ball 1 {};  '.format(bob1.pos))
c = wtext(text='theta1 {} radians \n'.format(theta1))
d = wtext(text='pos of ball 2 {};  '.format(bob2.pos))
e = wtext(text='theta2 {} radians \n'.format(theta2))

# Set up time ranges
tmin = 0
tmax = 50
step = 10000
dt = (tmax - tmin)/step

t = 0 #record the time

# Record the motion

while(t < tmax):
    d1 = bob1.pos.x - pivot1.x
    d2 = bob2.pos.x - pivot2.x
    a1 = (-m1*g*d1/Ls + k*(d2 - d1))/m1
    a2 = (-m2*g*d2/Ls - k*(d2 - d1))/m2

    v1 = v1 + a1*dt
    x1 = bob1.pos.x + v1*dt
    theta1 = x1 / Ls
    y1 = np.sqrt(Ls**2 - (x1 - pivot1.x)**2)

    v2 = v2 + a2*dt
    x2 = bob2.pos.x + v2*dt
    theta2 = x2 / Ls
    y2 = np.sqrt(Ls**2 - (x2 - pivot2.x)**2)\

    # Update the position of both balls
    bob1.pos = vector(x1, y1, 0)
    string1.axis = bob1.pos - pivot1
    bob2.pos = vector(x2, y2, 0)
    string2.axis = bob2.pos - pivot2

    spring.pos = bob1.pos
    spring.axis = bob2.pos - bob1.pos
    L = spring.length

    a.text='length of the spring: {} m \n'.format(L)
    b.text='pos of ball 1 {};  '.format(bob1.pos)
    c.text='theta1 {} radians \n'.format(theta1)
    d.text='pos of ball 2 {};  '.format(bob2.pos)
    e.text='theta2 {} radians \n'.format(theta2)

    rate(50)
    t = t + dt