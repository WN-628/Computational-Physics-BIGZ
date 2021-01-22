import numpy as np

xp = np.linspace(0, 10, 50)
yp = np.sin(xp)


def L_k(x, k, xp, yp):
    p = 1 #Initial value of the product
    i = 0 #Counter
    n = np.len(xp) #length of the pi notation
    while i < n:
        if i != k:
            p *= (x - xp[i]) / (x[k] - x[i])
        i += 1
    return p

def p_L(x, xp, yp):
    s = 0 #Initial value of the sum
    i = 0 #Counter
    n = np.len(xp) #length of the sum notation
    while i < n:
        s += yp[i]*L_k(x, i, xp, yp)
        i += 1


