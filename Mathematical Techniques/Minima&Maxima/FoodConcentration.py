#%%
import numpy as np
import matplotlib.pyplot as plt

def minima(xlow, xhigh, f, Nmax):
    n = 0
    phi = (1 + 5**(1/2)) / 2
    while(n < Nmax and xhigh - xlow > 10**-6):
        d = (phi - 1)*(xhigh - xlow)
        x1 = xlow + d
        x2 = xhigh - d
        if(f(x1) < f(x2)):
            xhigh = x2
        elif(f(x1) > f(x2)):
            xlow = x1
        n = n + 1
    print("The minima is ", f((xlow + xhigh) / 2), " when x = ", (xlow + xhigh) / 2)

g = lambda x : (x - 1)**2

minima(-1, 2, g, 500)