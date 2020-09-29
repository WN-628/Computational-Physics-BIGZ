# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:46:57 2020

@author: johnling
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

def f(t, T):
    if 0<t<(T/2):
        return 1
    elif t == T/2:
        return 0
    elif T/2<t<T:
        return -1

def S(t, n, T):
    s = 0;
    for i in range(1, n+1):
        a = 1/(2*i - 1)*np.sin((2*(2*i - 1)*np.pi*t)/T)
        s += a;
    s = 4/np.pi*s
    return s

T = 2*np.pi
t = np.linspace(0, 10, 1000)
f_list = []

for i in t :
    f_list.append(f(i, T))
    
plt.plot(t, S(t, 1, T))
plt.plot(t, S(t, 3, T))
plt.plot(t, S(t, 20, T))
plt.plot(t, S(t, 200, T))
plt.plot(t, f_list)
plt.show()