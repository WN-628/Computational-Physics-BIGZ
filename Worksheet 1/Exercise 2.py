# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:30:46 2020

@author: johnling
"""

import math as m

def tester (x, t):
    base = 1
    ans = 0
    
    true = m.sin(x)
    
    for i in range(t):
        result = (x**base) / m.factorial(base)
        if i%2 != 0:
            ans-= result
        else:
            ans+= result
        base+= 2    # base = base + 2
        
    e = (true - ans)/true * 100
    print(ans,true,e)
    
tester(0.9, 8)