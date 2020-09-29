# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:42:52 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 1000)

def f(x,t):
    y = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x - t))
    return y

plt.plot(x, f(x,0))