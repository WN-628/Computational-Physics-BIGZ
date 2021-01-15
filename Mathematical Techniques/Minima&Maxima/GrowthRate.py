# %%
def minima(xlow, xhigh, f, Nmax):
    n = 0
    phi = (1 + 5**(1/2)) / 2
    while(n < Nmax and xhigh - xlow > 10**-6):
        d = (phi - 1)*(xhigh - xlow)
        x1 = xlow + d
        x2 = xhigh - d
        if(f(x1) < f(x2)):
            xlow = x2
        elif(f(x1) > f(x2)):
            xhigh = x1
        n = n + 1
    return (xlow + xhigh) / 2
    print("The minima is ", f((xlow + xhigh) / 2), " when x = ", (xlow + xhigh) / 2)


#%%
import numpy as np
import matplotlib.pyplot as plt

g = lambda c : 2*c / (4 + 0.8*c + c**2 + 0.2*c**3)
f = lambda c : -2*c / (4 + 0.8*c + c**2 + 0.2*c**3)

c_arr = np.linspace(0, 50, 10000)
g_arr = []

for c in c_arr:
    g_arr.append(g(c))

plt.plot(c_arr, g_arr)
plt.show()

maxima = minima(0, 10, f, 100)
print("The maxima value is", g(maxima), "when x = ", maxima)



