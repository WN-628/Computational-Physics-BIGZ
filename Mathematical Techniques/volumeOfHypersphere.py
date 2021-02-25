#%%
import numpy as np
import math

def VHypersphere(D):
    N = 10000000
    # Create random sets of 2 number [a, b]
    points = 2*np.random.random((N, D)) - 1
    # Check the norm of the random sets of number is smaller than or not
    M = sum(np.linalg.norm(points, axis = 1) <= 1)
    print(points)
    print("Volumn is ", M/N*(2**D))

#%%

def AccurateVHypersphere(n, R):
    print(np.pi**(n / 2)*R**n / math.gamma(n/2 + 1))

AccurateVHypersphere(4, 1)