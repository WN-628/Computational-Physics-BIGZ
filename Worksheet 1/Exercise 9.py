# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:08:34 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
t = [0.6, 0.9, 1.1, 1.3, 1.4, 1.6, 1.7, 1.8, 1.9, 2.0]

def coe(x, y, deg):
    coeff = np.polyfit(x, y, deg)
    p = np.poly1d(coeff)
    print(p)
    y_fitted = p(x) 
    return y_fitted


plt.plot(t, l, 'o')
plt.plot(t, coe(t, l, 1))
plt.plot(t, coe(t, l, 2))
plt.plot(t, coe(t, l, 3))