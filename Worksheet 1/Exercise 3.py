# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:56:28 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

q_0 = 10
r = 60
l = 9
c = 0.00005

t = np.linspace(0, 0.8, 1000)

q = q_0*np.exp((-r*t)/(2*l))*np.cos(np.sqrt((1/(l*c))-((r/(2*l))**2))*t)

plt.plot(t,q)
plt.xlabel('t')
plt.ylabel('q')
plt.show()