# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:36:28 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def pathlength(x, y):
    L = 0
    for i in range (1, len(x)):
        L += np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return L

for k in range(2, 10):
    n = 2**k        
    i = np.linspace(0, n, n+2)
    x = 1/2*np.cos(2*np.pi*i/n)
    y = 1/2*np.sin(2*np.pi*i/n)
    leng = pathlength(x, y)
    print(leng)