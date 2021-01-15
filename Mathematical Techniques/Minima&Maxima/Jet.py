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
            xlow = x2
        elif(f(x1) > f(x2)):
            xhigh = x1
        n = n + 1
    print("The minima is ", f((xlow + xhigh) / 2), " when x = ", (xlow + xhigh) / 2)

#%%
A = 150
AR = 6.5
C_D0 = 0.018
rho = 0.413
W = 670*10**3
