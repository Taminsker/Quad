# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
import quadratures as q    # nos formules de quadrature
import fonctions_test as f # nos fonctions pour faire des tests
import otherfunction as of # les fonction py supplementaires ex : computeConvergenceOrder


method = [q.pt_milieu, q.trapeze, q.simpson]
method_name = ["pt_milieu", "trapezes", "Simpson"]


function_name = ["absWith", "abs", "exp", "cos", "arctan_der"]
function = [f.absWith, f.abs, f.exp, f.cos, f.arctan_der]
function_int = [f.absWith_int, f.abs_int, f.exp_int, f.cos_int, f.arctan_der_int]

a,b = -1., 1.        # l'intervalle
# On va faire l'approximation en découpant en 2^k morceaux pour k=0,1...k_max
k_max = 20
N = 2 ** np.arange (k_max) # pour avoir 2^{0,1,2,3,4...k_max}
h = (b - a) / N             # c'est aussi un tableau

Q = np.zeros_like (N, dtype = np.float64) # Alloue un tableau de la même
                                    # taille que N, initialisé à 0
E = np.zeros_like (N, dtype = np.float64) # pour les erreurs

O = np.zeros_like (N, dtype = np.float64) # ordre de convergence


for type in np.arange(1,6):
    print("\n### Methode : gauss_legendre_{}".format (type))
    plt.clf ()

    for k in np.arange(7):
        print("\n\n#### Test pour le monome de degré {}\n".format (k))
        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))

        f.degre = k # degré des monomes à tester
        I = f.monome_int (b) - f.monome_int (a) # intégrale exacte puisqu'on
                                            # connait une primitive
        # Calcul des quadratures et des erreurs
        # trapezes
        for i in np.arange (k_max):
            Q [i] = q.gauss_legendre(f.monome, a, b, N[i], type)
            E [i] = np.abs (I - Q[i])

            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format(N[i],I,Q[i],E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))
            if E [i] < 10. ** (-18):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

        # On peut tracer les courbes d'erreur
        plt.loglog(N,E,'+-',label="$x^{}$ o.c:{:.2}".format(k, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))


    for fun, fun_int, fun_name in zip (function, function_int, function_name):
        print ("\n\n#### Test pour f(x) = {}(x)\n".format (fun_name))
        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))


        I = fun_int (b) - fun_int (a)
        for i in np.arange (k_max):
            Q [i] = q.gauss_legendre (fun, a, b, N[i], type)
            E [i] = np.abs (I - Q[i])
            O [i] = 0.
            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format (N[i], I, Q[i], E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))
            if E [i] < 10. ** (-18):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

        # On peut tracer les courbes d'erreur
        plt.loglog (N, E, '+-', label = "{} o.c:{:.2}".format (fun_name, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))

    plt.title("Test de conv. méthode gauss_legendre_{} sur des f-tests [{}, {}]".format(type, a, b))
    plt.legend()
    plt.xlabel("N")
    plt.ylabel("Erreur")
    plt.grid()
    # Utilisez une des lignes ci-dessous pour voir/enregistrer le graphique
    # plt.show()
    plt.savefig("../img/gauss_legendre_{}.png".format (type))

# -------------------------------------------------------------------

for k in np.arange(7):
    print("\n\n#### Test pour le monome de degré {}\n".format (k))
    plt.clf ()
    for meth_q, meth_name in zip (method, method_name):
        print("\n### Methode : {}".format (meth_name))

        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))

        f.degre = k # degré des monomes à tester
        I = f.monome_int (b) - f.monome_int (a) # intégrale exacte puisqu'on
                                            # connait une primitive
        # Calcul des quadratures et des erreurs
        # trapezes
        for i in np.arange (k_max):
            Q [i] = meth_q (f.monome, a, b, N[i])
            E [i] = np.abs (I - Q[i])
            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format(N[i],I,Q[i],E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))
            if E [i] < 10. ** (-18):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

        # On peut tracer les courbes d'erreur
        plt.loglog(N,E,'+-',label="{} o.c:{:.2}".format(meth_name, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))

    for type in np.arange(1,6):
        print("\n### Methode : gauss_legendre_{}".format (type))
        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))

        f.degre = k # degré des monomes à tester
        I = f.monome_int (b) - f.monome_int (a) # intégrale exacte puisqu'on
                                            # connait une primitive
        # Calcul des quadratures et des erreurs
        # trapezes
        for i in np.arange (k_max):
            Q [i] = q.gauss_legendre (f.monome, a, b, N[i], type)
            E [i] = np.abs (I - Q[i])
            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format(N[i],I,Q[i],E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))
            if E [i] < 10. ** (-17):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

        # On peut tracer les courbes d'erreur
        plt.loglog(N,E,'+-',label="gauss_legendre_{} o.c:{:.2}".format(type, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))

    plt.title("Test de conv. de x**{} [{}, {}]".format(k, a, b))
    plt.legend()
    plt.xlabel("N")
    plt.ylabel("Erreur")
    plt.grid()
    # Utilisez une des lignes ci-dessous pour voir/enregistrer le graphique
    # plt.show()
    plt.savefig("../img/x{}_other.png".format (k))


for fun, fun_int, fun_name in zip (function, function_int, function_name):
    print ("\n\n#### Test pour f(x) = {}(x)\n".format (fun_name))
    plt.clf ()
    for meth_q, meth_name in zip (method, method_name):
        print("\n### Methode : {}".format (meth_name))
        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))


        I = fun_int (b) - fun_int (a)
        for i in np.arange (k_max):
            Q[i] = meth_q (fun, a, b, N[i])
            E[i] = np.abs (I - Q[i])
            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format (N[i], I, Q[i], E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))

            if E [i] < 10. ** (-17):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

            # On peut tracer les courbes d'erreur
        plt.loglog(N,E,'+-',label="{} o.c:{:.2}".format(meth_name, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))

    for type in np.arange(1,6):
        print("\n### Methode : gauss_legendre_{}".format (type))
        print ("{:^5s} | {:^14.8s} | {:^14.8s} | {:^14.8s}".format ("N[i]", "I", "Q[i]", "E[i]"))
        print ("{:-^5s} | {:-^14.8s} | {:-^14.8s} | {:-^14.8s}".format ("-", "-", "-", "-"))

        f.degre = k # degré des monomes à tester
        I = fun_int (b) - fun_int (a)
                                            # connait une primitive
        # Calcul des quadratures et des erreurs
        # trapezes
        for i in np.arange (k_max):
            Q [i] = q.gauss_legendre (fun, a, b, N[i], type)
            E [i] = np.abs (I - Q[i])
            # print ("{:5d} | {:14.8g} | {:14.8g} | {:14.8g}".format(N[i],I,Q[i],E[i]))
            print ("{:d} | {:g} | {:g} | {:g}".format (N[i], I, Q[i], E[i]))
            if E [i] < 10. ** (-17):
                E [i] = 0.
            if i > 0:
                if E [i - 1] == 0.:
                    E [i] = 0.

        # On peut tracer les courbes d'erreur
        plt.loglog(N,E,'+-',label="gauss_legendre_{} o.c:{:.2}".format(type, of.computeConvergenceOrder (E, N)))
        print ("Ordre de convergence moyen : {}".format (of.computeConvergenceOrder (E, N)))


    plt.title("Test de conv. de {} [{}, {}]".format(fun_name, a, b))
    plt.legend()
    plt.xlabel("N")
    plt.ylabel("Erreur")
    plt.grid()
    # Utilisez une des lignes ci-dessous pour voir/enregistrer le graphique
    # plt.show()
    plt.savefig("../img/{}_other.png".format (fun_name))
