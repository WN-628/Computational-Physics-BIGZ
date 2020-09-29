# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:58:18 2020

@author: johnling
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

a = 3
b = 2
Na = 10
Nb = 0
t0 = 0
tmax = 10
s = 100
t = np.linspace(t0, tmax, s)
dt = (tmax - t0)/s

def next_a(x):
    return x - x/a*dt

def next_b(x, y):
    return y + (x/a - y/b)*dt

def true_a(x):
    return Na*np.exp(-x/a)

def true_b(y):
    return Na/((1/b - 1/a)*a)*(np.exp(-y/a) - np.exp(-y/b))

Na_list = []
Nb_list = []
Na_true = []
Nb_true = []

for i in t:
    Nb_list.append(Nb)
    Nb = next_b(Na, Nb)
    Na_list.append(Na)
    Na = next_a(Na)
    
plt.plot(t, Na_list)
plt.plot(t, Nb_list)
plt.legend(['Na', 'Nb'])
plt.figure(0)
plt.show()

Na = 10
Nb = 0

for i in t:
    Nb_true.append(true_b(i))
    Na_true.append(true_a(i))

plt.plot(t, Na_true)
plt.plot(t, Nb_true)
plt.legend(['Na_true', 'Nb_true'])
plt.figure(1)
plt.show()

A_err = []
B_err = []

for i in range(len(t)):
    A_err.append(Na_list[i]-Na_true[i])
    B_err.append(Nb_list[i]-Nb_true[i])
    
plt.plot(t, A_err)
plt.plot(t, B_err)
plt.legend(['A_err', 'B_err'])
plt.figure(2)
plt.show()
    
    