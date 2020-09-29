# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:32:31 2020

@author: johnling
"""

import math
import numpy as np
import time

def t(t_0):
    M = 67
    c = 3.7
    rho = 1.038
    K = 5.4*10**(-3)
    Tw = 100
    Ty = 70
    t = (M**(2/3)*c*rho**(1/3))/(K*math.pi**2*(4*math.pi/3)**(2/3))*math.log(0.76*(t_0 - Tw)/(Ty - Tw))
    return time.strftime("%M:%S", time.gmtime(t)) 

print('t for a large egg taken from the fridgr is ' + t(4) + ', t for a large egg taken from room temperature is ' + t(20))