# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:59:59 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

sig = 3.4*10**(-10)
ep = 1.65*10**(-21)
r0 = 2**(1/6)*sig

r = np.linspace(r0*0.999,r0*1.001,50)

U = 4*ep*((sig/r)**12 - (sig/r)**6)

plt.plot(r,U)
plt.xlabel('r')
plt.ylabel('U')
plt.show()

F = 24*ep*sig**6*(2*sig**6/r**13 - 1/r**7)
plt.plot(r,F)
plt.xlabel('r')
plt.ylabel('F')
plt.show()

k = 24*ep*sig**6*((24*sig**6 - 7*r0**6)/r0**14)

U = -ep + 1/2*k*(r - r0)**2

plt.plot(r,U)
plt.xlabel('r')
plt.ylabel('U')
plt.show()