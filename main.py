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


def mod2coef(pol):
    coe = pol.all_coeffs()
    coe = np.asarray(coe) % 2
    coe = coe[::-1]
    for i in range(coe.shape[0], 7):
        coe = np.append(coe, [0])
    if coe.shape[0] > 7:
        coe = np.delete(coe, 7)
    return coe


def polynom7(coe):
    x = symbols('x')
    if (coe[1] == coe[2] == coe[3] == coe[4] == coe[5] == coe[6] == 0) & (coe[0] == 1):
        return 1
    if (coe[1] == coe[2] == coe[3] == coe[4] == coe[5] == coe[6] == coe[0] == 0):
        return 0
    return sp.poly(
        1 * coe[0] + x * coe[1] + x ** 2 * coe[2] + x ** 3 * coe[3] + x ** 4 * coe[4] + x ** 5 * coe[5] + x ** 6 *
        coe[6])


def coding():
    print("Кодирование:")
    x = symbols('x')
    a = a4()
    g = g74()
    print("a(x)=", a)
    print("g(x)=", g)
    v = a * g
    coe = mod2coef(v)
    print("v=", coe)
    v = polynom7(coe)
    print("v(x)=", v)


def decoding():
    print("Декодирование:")
    x = symbols('x')
    g = g74()
    w = np.array([1, 0, 0, 0, 0, 0, 0])
    n = w.shape[0]
    print("Ошибка:", w)
    w = polynom7(w)
    print("w(x)=", w)
    s_x = w % g
    s_x = mod2coef(s_x)
    s_x = polynom7(s_x)
    print("s(x)=", s_x)
    for i in range(0, n):
        s_i = (x ** i * s_x) % g
        s_i = mod2coef(s_i)
        s_i = polynom7(s_i)
        print("i=", i, "s_i=", s_i)
        if s_i == 1:
            e = x ** (n - i) * s_i
            we = sp.poly(w + e)
            res = mod2coef(we)
            print("w+e=", res)
            res = polynom7(res)
            print("w(x)+e(x)=", res)
            return res
        if i == n - 1:
            pprint("Исправление ошибки невозможно(")


if __name__ == '__main__':
    cod = coding()
    decod = decoding()
