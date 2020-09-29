# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:13:43 2020

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