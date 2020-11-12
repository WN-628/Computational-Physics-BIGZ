#%%
# from vpython import sphere
# from vpython import vector

# import vpython
# print(dir(vpython))
# sphere(radius = 0.5, pos = vector(1,2,3))
# %%
# from vpython import sphere, vector, color
# L = 5
# R = 0.3
# for i in range(-L, L + 1):
#     for j in range(-L, L + 1):
#         for k in range(-L, L - 5):
#             sphere(pos = vector(i, j, k), radius = R)

#%%
# from vpython import box, cone, cylinder, pyramid, arrow, vector

# box(pos = vector(x, y, z), axis = vector(a, b, c),  \
#     length = L, height = H, width = W, up = vector(q, r, a))
# cone(pos = vector(x, y, z), axis = vector(a, b, c), radius = R)
# cylinder(pos = vector(x, y, z), axis = vector(a, b, c), radius = R)
# pyramid(pos = vector(x, y, z), size = vector(a, b, c))
# arrow(pos = vector(x, y, z), axis = vector(a, b, c), \
#     headwidth = H, headlength = L, shaftwidth = W)

#%%
# from vpython import sphere, vector
# s = sphere(pos = vector(0, 0, 0))
# s.pos = vector(1, 4, 3)

#%%
from vpython import sphere, rate, vector
import numpy as np
s = sphere(pos = vector(1, 0, 0), radius = 0.1)
for theta in np.arange(0, 10*np.pi, 0.1):
    rate(30)
    x = np.cos(theta)
    y = np.sin(theta)
    s.pos = vector(x, y, 0)