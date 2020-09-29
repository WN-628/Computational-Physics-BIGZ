# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:10:40 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

a = 5.5289*10**(-8)
b = 8.5016*10**(-6)
c = 6.5622*10**(-5)

T_c = np.linspace(0,100,10000)
rho = a*T_c**3 - b*T_c**2 + c*T_c + 0.99987

plt.plot(T_c, rho)
plt.xlabel('T_c')
plt.ylabel('rho')
plt.show()