# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:55:48 2020

@author: johnling
"""

import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 1
t0 = 0
tmax = 10
n = 1000
t = np.linspace(t0, tmax, n)
dt = (tmax - t0)/n
v = 100

v_list = []

def next_v(x):
    return x + (a - b*x)*dt

for i in t:
    v_list.append(v)
    v = next_v(v)

plt.plot(t, v_list)
plt.figure(0)
plt.show()
