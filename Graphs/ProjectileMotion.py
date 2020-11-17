#%% 
from numpy import *
from matplotlib.pyplot import *
from vpython import *

# Initialize the objects
ball = sphere(pos = vector(0, 0.1, 0), radius = 0.1)
floor = box(pox = vector(0, 0, 0), size = vector(1, 0.05, 1), color = color.blue)

# Set up initial conditions
ball.velocity = vector(0, 5, 0)
ball.mass = 0.25
ball.p = ball.velocity*ball.mass
g = vector(0, -9.8, 0)
Fnet = g*ball.mass
dt = 0.001
t = 0
# Initialize for air resistance
c = 0.5
rho = 1.2
A = pi*ball.radius**2
Fnet = (g*ball.mass - 0.5*rho*c*A*mag(ball.p/ball.mass)**2*ball.p/mag(ball.p))

while t < 4:
    rate(300)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    ball.p = ball.p + Fnet*dt
    t = t*dt

    if ball.pos.y < (floor.pos.y + ball.radius):
        ball.p = -ball.p

posgraph = gcurve(color = color.green)
posgraph.plot(pos = (t, ball.pos.y))