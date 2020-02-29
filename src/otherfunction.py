# -*- coding: utf-8 -*-

import numpy as np
import math

def computeConvergenceOrder (E, N):
    """ computeConvergenceOrder : moyenne sur les pentes dans le repere loglog pour trouver l'ordre de convergence de la méthode"""

    oc = 0.
    k = 0.

    for i in np.arange (E.size):
        if math.isnan (E [i]):
            continue
        if math.isinf (E [i]):
            continue
        if E [i] == 0.:
            continue
        if i > 0:
            if math.isnan (E [i - 1]):
                continue
            if math.isinf (E [i - 1]):
                continue
            if E [i - 1] == 0.:
                continue

            oc = oc + (np.log (E [i]) - np.log (E [i - 1])) / (np.log (N [i]) - np.log (N [i - 1]))
            k = k + 1.
    if k == 0.:
        return np.nan
    if oc / k == 0.:
        return np.nan
    return np.abs (oc / k)
