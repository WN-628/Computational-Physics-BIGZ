# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:15:34 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def logistic(x, r):
    return r*x*(1 - x)

r = float(input('r?'))

x_List = []
x = 0.5

for i in range(100):
    x_List.append(logistic(x, r))
    x = logistic(x, r)
    
plt.plot(range(1, 101), x_List)
plt.show()
