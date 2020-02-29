# -*- coding: utf-8 -*-

import math
import numpy as np

# On définit ici des fonctions qui permettent de vérifier la précision
# et l'ordre de convergence des formules de quadrature. Pour chaque
# fonction, on définit donc sa primitive.

degre = 0 # degré des polynôme

def monome(x):
    """fonction monome x^k, pour vérifier l'ordre théorique des
    quadratures. Par défaut k=0.

    """
    return x**degre

def monome_int(x):
    """primitive de la fonction x^k. Par défaut k=0."""

    return x**(degre+1)/(degre+1.)

def absWith(x):
    return np.abs(np.longdouble(x - math.pi / 10.))

def absWith_int(x):
    return np.longdouble(0.5 * ( x - math.pi / 10.) * np.abs(x - math.pi /10.))

def abs(x):
    return np.abs(np.longdouble(x));

def abs_int(x):
    return np.longdouble(0.5 * x * np.abs(np.longdouble(x)))

def cos(x):
    return np.cos(np.longdouble(x))

def cos_int(x):
    return np.sin(np.longdouble(x))

def exp(x):
    return np.exp(np.longdouble(x))

def exp_int(x):
    return np.exp(np.longdouble(x))

def arctan_der(x):
    return np.longdouble(1. / ( 1 + x**2))

def arctan_der_int(x):
    return np.arctan(np.longdouble(x))
