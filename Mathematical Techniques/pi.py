#%%
import numpy as np

N = 10000000
# Create random sets of 2 number [a, b]
points = 2*np.random.random((N, 2)) - 1
# Check the norm of the random sets of number is smaller than or not
M = sum(np.linalg.norm(points, axis = 1) <= 1)

print("pi is", M/N*4)
# %%
