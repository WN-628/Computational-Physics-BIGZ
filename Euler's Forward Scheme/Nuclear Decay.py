# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:47:06 2020

@author: johnling
"""
#%%
import numpy as np
import matplotlib.pyplot as plt


lamb = 0.693
t0 = 0
tmax = 10
n = 100
s = 100
t = np.linspace(t0, tmax, s)
dt = (tmax - t0)/s

def next_n(n):
    return n - lamb*n*dt

def true_n(n, tt):
    return n*np.exp(-lamb*tt)

N_list = []

N_true = []

for i in t:
    N_list.append(n)
    n = next_n(n)
    
a = 100
for i in t:
    N_true.append(a)
    a = true_n(a, i)
    
Err = []

for i in range(len(t)):
    Err.append(N_list[i]-N_true[i])
    

plt.plot(t, N_list)
plt.plot(t, N_true)
plt.figure(0)
plt.show()

plt.plot(t, Err)
plt.figure(1)
plt.show()
# %%
