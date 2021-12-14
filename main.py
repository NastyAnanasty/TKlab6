import numpy as np
import sympy as sp
from sympy import *


# -------------------6.1----------------------------
def g74():
    x = symbols('x')
    return sp.poly(1 + x ** 2 + x ** 3)


def koeff_g74():
    return np.array([[1, 0, 1, 1, 0, 0, 0]])


def a4():
    a = np.random.randint(0, 2, (1, 4))
    # a = np.array([[1, 0, 0, 1]])
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
        coe[0] = (coe[0] + 1) % 2
    return coe


def polynom7(coe):
    x = symbols('x')
    if (coe[1] == coe[2] == coe[3] == coe[4] == coe[5] == coe[6] == 0) and (coe[0] == 1):
        return 1
    if coe[1] == coe[2] == coe[3] == coe[4] == coe[5] == coe[6] == coe[0] == 0:
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
    return v


def decoding():
    v = coding()
    print("Декодирование:")
    x = symbols('x')
    g = g74()
    mistake = np.array([1, 0, 0, 0, 0, 0, 0])
    n = mistake.shape[0]
    print("Ошибка:", mistake)
    mistake = polynom7(mistake)
    w = v + mistake
    w = mod2coef(w)
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
        if s_i == 1 or s_i == 0:
            e = x ** (n - i) * s_i
            we = sp.poly(w + e)
            res = mod2coef(we)
            print("w+e=", res)
            res = polynom7(res)
            print("w(x)+e(x)=", res)
            return res
        if i == n - 1:
            pprint("Исправление ошибки невозможно(")


# -------------------------------------------------

# -------------------6.2----------------------------

def g15_9():
    x = symbols('x')
    return sp.poly(1 + x ** 3 + x ** 4 + x ** 5 + x ** 6)


def koeff_g15_9():
    return np.array([1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])


def a9():
    a = np.random.randint(0, 2, (1, 9))
    print("a=", a)
    x = symbols('x')
    return sp.poly(1 * a[0, 0] + x * a[0, 1] + x ** 2 * a[0, 2] + x ** 3 * a[0, 3] + x ** 4 * a[0, 4]
                   + x ** 5 * a[0, 5] + x ** 6 * a[0, 6] + x ** 7 * a[0, 7] + x ** 8 * a[0, 8], x)


def polynom15(coe):
    x = symbols('x')
    return sp.poly(
        1 * coe[0] + x * coe[1] + x ** 2 * coe[2] + x ** 3 * coe[3] + x ** 4 * coe[4] + x ** 5 * coe[5] + x ** 6 *
        coe[6] + x ** 7 * coe[7] + x ** 8 * coe[8] + x ** 9 * coe[9] + x ** 10 * coe[10] + x ** 11 * coe[11]
        + x ** 12 * coe[12] + x ** 13 * coe[13] + x ** 14 * coe[14], x)


def mod2coef_n(pol, n):
    coe = pol.all_coeffs()
    coe = np.asarray(coe) % 2
    coe = coe[::-1]
    for i in range(coe.shape[0], n):
        coe = np.append(coe, [0])
    if coe.shape[0] > n:
        coe = np.delete(coe, n)
        coe[0] = (coe[0] + 1) % 2
    return coe


def coding_2():
    print("Кодирование:")
    a = a9()
    g = g15_9()
    print("a(x)=", a)
    print("g(x)=", g)
    v = a * g
    coe = mod2coef_n(v, 15)
    print("v=", coe)
    v = polynom15(coe)
    print("v(x)=", v)
    return v


def errors_package():
    x = symbols('x')
    return np.array([
        sp.poly(1, x),
        sp.poly(1 + x),
        sp.poly(1 + x ** 2),
        sp.poly(1 + x + x ** 2)
    ])


def decoding_2():
    v = coding_2()
    print("Декодирование:")
    x = symbols('x')
    g = g15_9()
    errors = errors_package()
    mistake = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n = mistake.shape[0]
    print("Ошибка:", mistake)
    mistake = polynom15(mistake)
    w = v + mistake
    w = mod2coef(w)
    w = polynom7(w)
    print("w(x)=", w)
    s_x = w % g
    s_x = mod2coef_n(s_x, 15)
    s_x = polynom15(s_x)
    print("s(x)=", s_x)
    for i in range(0, n):
        s_i = (x ** i * s_x) % g
        s_i = mod2coef_n(s_i, 15)
        s_i = polynom15(s_i)
        print("i=", i, "s_i=", s_i)
        if s_i in errors:
            e = x ** (n - i) * s_i
            we = sp.poly(w + e)
            res = mod2coef_n(we, 15)
            print("w+e=", res)
            res = polynom15(res)
            print("w(x)+e(x)=", res)
            return res
        if i == n - 1:
            pprint("Исправление ошибки невозможно(")


# --------------------------------------------------

if __name__ == '__main__':
    # -------------6.1---------------
    decoding()
    # -------------6.2---------------
    decoding_2()
