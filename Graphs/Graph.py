#%% 
import numpy as np
import matplotlib.pyplot as plt
import pylab as lab

data = lab.loadtxt("circular.txt", float)
lab.imshow(data)
lab.imshow(data,origin="lower", extent = [0, 10, 0, 5], aspect = 2.0)
lab.jet()
lab.show()


# %%

