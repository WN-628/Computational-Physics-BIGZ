#%%
# import package that is needed
import numpy as np
from vpython import *

# https://physicscatalyst.com/graduation/coupled-pendulums/

# Constant
m1 = 5 # Mass of the ball at the left (kg)
m2 = 10 # Mass of the ball at the right (kg)
Ls = 10 # Length of the string (m)
L0 = 10 # Original length of the spring (m)
L = L0 # Instant length of the spring(m)
k = 20 # Spring constant (kg / s^2)
g = 9.8 # Gravitational constant
theta1 = np.pi/6 # The angle for the first ball
theta2 = np.pi/10 # The angle for the second ball

# Initialize the objects
canvas(width = 1280, height = 720) # For 1080p screen
# canvas(width = 3840, height = 2160) # For 4k screen
pivot = vector(0, 20, 0)
pivot1 = vector(-5, 20, 0)
pivot2 = vector(5, 20, 0)
bob1 = sphere(pos = vector(pivot1.x + Ls*np.sin(theta1), pivot1.y - Ls*np.cos(theta1), 0), radius = 0.5)
string1 = cylinder(pos= pivot1, axis = bob1.pos - pivot1, radius=0.05)
bob2 = sphere(pos = vector(pivot2.x + Ls*np.sin(theta2), pivot2.y - Ls*np.cos(theta2), 0), radius = 0.5)
string2 = cylinder(pos= pivot2, axis = bob2.pos - pivot2, radius=0.05)
Ceiling = box(pos = pivot, size = vector(20, 0.5, 20), color = color.green)
spring = helix(pos = bob1.pos, axis = bob2.pos - bob1.pos, radius = 0.3, coils = 20)
L = ((bob2.pos.x - bob1.pos.x)**2 + (bob2.pos.y - bob1.pos.y)**2)
lengthDisp = wtext(text='length of the spring: {} m \n'.format(L))
lengthDisp = wtext(text='pos of ball 1 {};  '.format(bob1.pos))
lengthDisp = wtext(text='theta1 {} radians \n'.format(theta1))
lengthDisp = wtext(text='pos of ball 2 {};  '.format(bob2.pos))
lengthDisp = wtext(text='theta2 {} radians \n'.format(theta2))

# Set up time ranges


# Record the motion