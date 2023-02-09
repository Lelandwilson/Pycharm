import numpy as np
from scipy.optimize import fsolve
from math import*
def func1(z):
    x=z[0]
    F = np.empty((1))
    F[0] = (x+pi/4) + sin(x)+(1/8)*sin(3*x)
    return(F)

zGuess = np.array([0.88])
z = fsolve(func1, zGuess)
print(z)
