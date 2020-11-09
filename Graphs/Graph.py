#%% 
import numpy as np
import matplotlib.pyplot as plt
import pylab as lab

data = lab.loadtxt("circular.txt", float)
lab.imshow(data)
lab.imshow(data, origin = "lower")
lab.jet()
lab.show()


# %%

