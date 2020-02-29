# -*- coding: utf-8 -*-

import numpy as np

def pt_milieu (f, a, b, n):
    """Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b - a) / n
    x = a + np.arange (n) * h
    Q = h * np.sum (f (x + h / 2.))
    return Q

def trapeze (f, a ,b, n):
    """ Quadrature de \int_a^b f(x)dx par la méthode des trapèzes sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b - a) / n
    x = a + np.arange (n) * h
    Q = h / 2. * np.sum (f (x) + f (x + h))
    return Q

def simpson (f, a, b, n):
    """ Quadrature de \int_a^b f(x)dx par la méthode de Simpson sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b - a) / n
    x = a + np.arange (n) * h
    Q = h / 6. * np.sum (f (x) + 4 * f (x + h / 2.) + f (x + h))
    return Q

def gauss_legendre_2 (f, a, b, n):
    """ Quadrature de \int_a^b f(x)dx par la méthode de Gauss-Legendre _2 sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b - a) / n
    x = a + np.arange (n) * h
    Q = h / 2. * np.sum(f (x - np.sqrt (3) / 6. * h ) + f (x + np.sqrt (3) / 6. * h))
    return Q

def gauss_legendre_3 (f, a, b, n):
    """ Quadrature de \int_a^b f(x)dx par la méthode de Gauss-Legendre _3 sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b - a) / n
    x = a + np.arange (n) * h
    value = np.sqrt (15) / 10.
    Q = h / 2. * np.sum (5. / 9. * f (x - value * h + h / 2.) + 8. / 9. * f (x) + 5. / 9. * f (x + value * h + h / 2.))
    return Q

def gauss_legendre (f, a, b, n, type):

    if type == 1:
        x_i = np.array ([0.])
        w_i = np.array ([2.])

    elif type == 2:
        var_1 = 0.577350269189625764509148780502
        x_i = np.array ([- var_1, var_1])
        w_i = np.array ([1., 1.])

    elif type == 3:
        var_1 = 0.774596669241483377035853079956
        x_i = np.array ([- var_1, 0., var_1])
        var_2 = 0.555555555555555555555555555556
        var_3 = 0.888888888888888888888888888889
        w_i = np.array ([var_2, var_3, var_2])

    elif type == 4:
        var_1 = 0.861136311594052575223946488893
        var_2 = 0.339981043584856264802665759103
        x_i = np.array ([- var_1, - var_2, var_2, var_1])

        var_3 = 0.347854845137453857373063949222
        var_4 = 0.652145154862546142626936050778
        w_i = np.array ([var_3, var_4, var_4, var_3])

    else :
        var_1 = 0.906179845938663992797626878299
        var_2 = 0.538469310105683091036314420700
        x_i = np.array ([- var_1, - var_2, 0.,  var_2, var_1])

        var_3 = 0.23692688505618908751426404072
        var_4 = 0.478628670499366468041291514836
        var_5 = 0.568888888888888888888888888889
        w_i = np.array ([var_3, var_4, var_5, var_4, var_3])

    h = (b - a) / n
    A = np.zeros ((type, n))
    x = a + np.arange (n + 1) * h

    for i in np.arange (type):
        A [i] = w_i [i]  * f (h / 2. * x_i [i] + (x [:-1] + x [1:]) / 2.)

    Q = h / 2. * np.sum (A)
    return Q
