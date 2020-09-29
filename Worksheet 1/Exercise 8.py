# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:49:46 2020

@author: johnling
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

phi = (1 + np.sqrt(5))/2
for k in range(1, 50000, 1):
    s = np.linspace(1, k, 500)
    r = np.sqrt(s)
    theta = 2*np.pi*s/phi
    plt.polar(theta, r)
    plt.show()