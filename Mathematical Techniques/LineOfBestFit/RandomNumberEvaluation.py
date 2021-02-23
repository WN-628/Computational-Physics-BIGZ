#%%
import random

humps_func = lambda x: 1/((x-0.3)**2+0.01)+1/((x-0.9)**2+0.04)-6

maximum = humps_func(0)

for i in range(0, 1000000):
    randnum = random.uniform(0, 2)
    if humps_func(randnum) > maximum:
        maximum = humps_func(randnum)

print(maximum)