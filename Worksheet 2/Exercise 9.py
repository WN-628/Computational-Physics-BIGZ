# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 08:57:25 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def gvalue(x, n):
    return np.sin(x)/(x**n)

x = np.linspace(-5, 5, 100)
n1_list = []
n2_list = []
n3_list = []

for i in x:
    n1_list.append(gvalue(i, 1))
    n2_list.append(gvalue(i, 2))
    n3_list.append(gvalue(i, 3))
    
plt.plot(x, n1_list)
plt.plot(x, n2_list)
plt.plot(x, n3_list)
plt.ylim([-10, 10])
plt.show()
