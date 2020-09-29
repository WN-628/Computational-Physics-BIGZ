# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:08:10 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as pltimport math as m
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = np.exp(x)
    return y
    
def diff(f, x, h=1e-5):
    di = (f(x+h) - f(x-h))/(2*h)
    return di

print(diff(f, 0, h=1e-5))

print(diff(lambda x: np.exp(-2*x**2), 0, h=1e-5))

print(diff(lambda x: np.exp(-x), 0, h=1e-5))

print(diff(lambda x: np.cos(x), 2*np.pi, h=1e-5))

print(diff(lambda x: np.log(x), 1, h=1e-5))