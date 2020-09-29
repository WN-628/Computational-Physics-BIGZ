# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:52:16 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def v(x, mu, exp):
    y = (1 - exp(x/mu))/(1 - exp(1/mu))
    n = 1 - exp(x/mu)
    d = 1 - exp(1/mu)
    print(y, n, d)
    return[y, n, d]

x_list = np.linspace(0, 1, 100)
mu = 1e-3

#for x in x_list:
#    print(v(x, mu, m.exp))
#    print(v(x, mu, np.exp))
    
x = np.linspace(0, 1, 10000)
plt.plot(x, v(x, 1, np.exp)[0])
plt.plot(x, v(x, 0.1, np.exp)[0])
plt.plot(x, v(x, 0.01, np.exp)[0])
plt.show()