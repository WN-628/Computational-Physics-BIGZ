# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:16:17 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

x0 = 0
x1 = 3*np.pi/2
xaxis = np.linspace(x0,x1,10000)

def cosf(domain):
    cos = 0
    count = 1
    for i in range(0,9,2):
        num = (domain**i) / (m.factorial(i))
        if count != 1 and count % 2 == 0:
            cos -= num
        else: 
            cos += num
        count += 1
    return cos

y = cosf(xaxis)
plt.plot(xaxis, y, 'b-')
plt.plot(xaxis, np.cos(xaxis), 'r-')
plt.legend(['Approximation', 'True'])
plt.show()