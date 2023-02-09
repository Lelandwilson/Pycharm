import numpy as np
import scipy.integrate as integrate
import math

# Non-periodic sawtooth function defined for a range [-l,l]
def sawtooth(x):
    return x
# Non-periodic square wave function defined for a range [-l,l]
def square(x):
    if x > 0:
        return np.pi
    else:
        return -np.pi

# Non-periodic triangle wave function defined for a range [-l,l]
def triangle(x):
    if x > 0:
        return x
    else:
        return -x

# Non-periodic cycloid wave function defined for a range [-l,l]
def cycloid(x):
    return np.sqrt(np.pi ** 2 - x ** 2)

def fourier(li, lf, n, f):
    l = (lf - li) / 2
    # Average
    a0 = 1 / l * integrate.quad(lambda x: f(x)*math.sin(x), li, lf)[0]
    # Cos coef
    an = np.zeros((n))
    # Sin coef
    bn = np.zeros((n))

    for i in range(1, n + 1):
        an[i - 1] = 1 / l * integrate.quad(lambda x: f(x) * np.cos(i * np.pi * x / l), li, lf)[0]
        bn[i - 1] = 1 / l * integrate.quad(lambda x: f(x) * np.sin(i * np.pi * x / l), li, lf)[0]

    return [a0 / 2.0, an, bn]


if __name__ == "__main__":
    # Limits for the functions
    li = -np.pi
    lf = np.pi

    # Number of harmonic terms
    n = 3

    # # Fourier coeffficients for various functions
    # coeffs = fourier(li, lf, n, sawtooth)
    # print('Fourier coefficients for the Sawtooth wave\n')
    # print('a0 =' + str(coeffs[0]))
    # print('an =' + str(coeffs[1]))
    # print('bn =' + str(coeffs[2]))
    # print('-----------------------\n\n')

    coeffs = fourier(li, lf, n, square)
    print('Fourier coefficients for the Square wave\n')
    print('a0 =' + str(coeffs[0]))
    print('an =' + str(coeffs[1]))
    print('bn =' + str(coeffs[2]))
    print('-----------------------\n\n')

    # coeffs = fourier(li, lf, n, triangle)
    # print('Fourier coefficients for the Triangular wave\n')
    # print('a0 =' + str(coeffs[0]))
    # print('an =' + str(coeffs[1]))
    # print('bn =' + str(coeffs[2]))
    # print('-----------------------\n\n')

    # coeffs = fourier(li, lf, n, cycloid)
    # print('Fourier coefficients for the Cycloid wave\n')
    # print('a0 =' + str(coeffs[0]))
    # print('an =' + str(coeffs[1]))
    # print('bn =' + str(coeffs[2]))
    # print('-----------------------\n\n')
