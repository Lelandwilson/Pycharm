from math import sin, cos, exp, pi
from scipy.integrate import quad
import scipy.integrate as integrate
import numpy as np

#f(x) = 4, 0<= x <= 3
F_of_X = 4
_L = 0 #lower limit
L = 3 #upper limit

def a0(x):
    return ((2/L)*F_of_X)

def an(x):
    n = 1
    return ((2/L)*F_of_X*cos((n*pi*F_of_X)/L))

def bn(x):
    n = 1
    return ((2/L)*F_of_X*sin((n*pi*x)/L))

#calc a0
print("a0:")
print("\t"+str(quad(a0, _L,L)[0]))


#calc an
print("an")
print("\t"+str(quad(an, _L,L)[0]))
# print(2 / L * integrate.quad(lambda x: F_of_X * np.cos(1 * np.pi * x / L), _L, L)[0])

#calc bn
print("bn")
print("\t"+str(quad(bn, _L,L)[0]))