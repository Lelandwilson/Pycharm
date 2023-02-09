import numpy as np
from scipy.optimize import fsolve
#instead of cramers or gauss elimination

def myFunc(w):
    x = w[0]
    y = w[1]
    z = w[2]

    F = np.empty((3))
    F[0] = x+8*y+3*z+31
    F[1] = 3*x-2*y+z+5
    F[2] = 2*x-3*y+2*z-6
    return(F)

wGuess = np.array([1,8,3])
w = fsolve(myFunc, wGuess)
print(w)