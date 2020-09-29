# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:02:44 2020

@author: johnling
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
import math as m

a = 10
b = 3
N = 500
t0 = 0
tmax = 10
s = 100
t = np.linspace(t0, tmax, s)
dt = (tmax - t0)/s

def next_N(x):
    return (a - b*x)*x*dt + x

N_list = []

for i in t:
    N_list.append(N)
    N = next_N(N)

plt.plot(t, N_list)
plt.legend(['N'])
plt.figure(0)
plt.show()
