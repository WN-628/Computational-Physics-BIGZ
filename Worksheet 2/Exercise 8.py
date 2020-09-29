# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:09:00 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

g = 9.8

m = float(input('m?'))
v0 = float(input('v0?'))

t = np.linspace(0, 2*v0/g)

P_list = []
K_list = []
H_list = []

def y(t):
    return (v0*t - 1/2*g*t**2)

for i in t:
    P_list.append(m*g*y(i))
    K_list.append(1/2*m*(v0 - g*i)**2)
    H_list.append(m*g*y(i)+1/2*m*(v0 - g*i)**2)

plt.plot(t, P_list)
plt.plot(t, K_list)
plt.plot(t, H_list)
plt.show()