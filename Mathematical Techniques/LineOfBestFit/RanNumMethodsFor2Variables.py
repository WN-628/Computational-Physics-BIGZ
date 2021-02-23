#%% two-dimensional function
import random
two_dimen_func = lambda x,y: y-x-2*x**2-2*x*y-y**2

maximum = two_dimen_func(-2, 1)
x = -2
y = 1

for i in range(0, 1000000000):
    randx = random.uniform(-2, 2)
    randy = random.uniform(1, 3)
    if two_dimen_func(randx, randy) > maximum:
        maximum = two_dimen_func(randx, randy)
        x = randx
        y = randy
    
print("maximum", maximum)
print("x", x)
print("y", y)