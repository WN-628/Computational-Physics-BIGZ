# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:58:24 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

a = 10
x_old = 5
i = 0

def x_new(x_old):
    return (x_old + a/x_old)/2

def er(x_new, x_old):
    return np.abs((x_new - x_old)/x_new)
    
while er(x_new(x_old), x_old) >= 0.01:
    i = i+1 
    x_old = x_new(x_old)

#print(x_old, i, er(x_new(x_old), x_old))

a_list = np.linspace(1, 1000000000)
i_list = []

for a in a_list:
    i = 0
    x_old = a/2
    while er(x_new(x_old), x_old) >= 0.01:
        i = i+1 
        x_old = x_new(x_old)
    i_list.append(i)
    
plt.semilogx(a_list, i_list)
plt.show()