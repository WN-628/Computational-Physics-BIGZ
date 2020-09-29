# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:01:42 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,10000)

def Gauss(sig):
    g = 1/(sig*np.sqrt(2*np.pi))*np.exp(-x**2 / (2*sig**2))
    return g


plt.plot(x, Gauss(1), 'b-')
plt.plot(x, Gauss(1.5), 'r-')
plt.plot(x, Gauss(2), 'g-')
plt.legend(['sig = 1', 'sig = 1.5', 'sig = 2'])
plt.show()