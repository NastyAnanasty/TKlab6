import numpy as np
import sympy as sp
from sympy import *


def g74():
    x = symbols('x')
    return sp.poly(1 + x ** 2 + x ** 3)


def koeff_g74():
    return np.array([[1, 0, 1, 1, 0, 0, 0]])


def a4():
    # a = np.random.randint(0, 2, (1, 4))
    a = np.array([[1, 0, 0, 1]])
    print("a=", a)
    x = symbols('x')
    return sp.poly(1 * a[0, 0] + x * a[0, 1] + x ** 2 * a[0, 2] + x ** 3 * a[0, 3])


def coding():
    print("Coding:")
    x = symbols('x')
    a = a4()
    g = g74()
    print("a(x)=", a)
    print("g(x)=", g)
    v = a * g
    coe = v.all_coeffs()
    coe = np.asarray(coe) % 2
    coe = coe[::-1]
    print("v=", coe)
    v =sp.poly(
        1 * coe[0] + x * coe[1] + x ** 2 * coe[2] + x ** 3 * coe[3] + x ** 4 * coe[4] + x ** 5 * coe[5] + x ** 6 *
        coe[6])
    print("v(x)=", v)


def decoding():
    print("Decoding:")
    x = symbols('x')
    g = g74()
    w = np.array([[1, 1, 0, 0, 0, 0, 1]])
    print("Ошибка:", w)
    w = sp.poly(
        1 * w[0, 0] + x * w[0, 1] + x ** 2 * w[0, 2] + x ** 3 * w[0, 3] + x ** 4 * w[0, 4] + x ** 5 * w[0, 5] + x ** 6 *
        w[0, 6])
    print("w(x)=", w)
    s = w % g
    print(s)


if __name__ == '__main__':
    cod = coding()
    decod =decoding()
