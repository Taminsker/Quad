$$x_{1,2} = {-b\pm\sqrt{b^2 - 4ac} \over 2a}.$$

# Première initiation à git en programmant des formules de quadrature en python

Ce fichier fait office de compte rendu. Il doit donc être mis à jour au
cours de la séance, au fur et à mesure que vous réalisez le travail. Les
fichiers modifiés et ajoutés font évidemment partie du travail.

C'est la version du mardi 17 septembre 2019 à 23h et son historique qui
sera notée.

*Il n'est pas nécessaire d'aller au bout des questions (le travail est
adapté à vos expériences de programmation, qui sont très
variables). C'est l'effort dans l'utilisation des outils (git et python)
qui est valorisé.*

**À la fin de votre travail, il est donc capital de pousser (*git push*)
  vos modifications sur le serveur, afin que je puisse les voir**

*Rappel:* prenre connaissance, brièvement, du [langage
Markdown](https://guides.github.com/features/mastering-markdown) propre
à la plateforme Github.

Si vous lisez ceci, c'est que vous avez:

- un compte sur la plateforme github.com, et un email validé de l'
  Université

- accepté le lien envoyé sur votre messagerie étudiante, et ainsi obtenu
  la création automatique d'un dépôt git contenant le descriptif du
  travail à réaliser (ce fichier).

## Première partie: environnement de travail et initiation à Python

1. Une fois le dépôt créé, vous le voyez sur votre compte github (en
ligne). Vous pouvez donc récupérer l'adresse et télécharger le dépôt
pour commencer à travailler (*git clone <url à récupérer en ligne>*).
*Fait.*

2. N'oubliez pas de configurer git si nécessaire (*git config --list,
git config --local user.{name,email}*).
*Fait.*

3. Préparez votre environnement de travail: éditeur de texte (*emacs*,
*vim*, *atom*...) et terminaux (terminal par défaut du système, pour git
et pour l'interpréteur *ipython3*), ou bien environnement de
développement intégré (comme *spyder3*). Pouvez-vous détailler
ci-dessous votre choix d'environnement de travail ?

*J'utilise Atom avec le terminal à côté.*

4. Puisque vous avez apporté des modifications cohérentes (réponse à la
question 3. ci-dessus), validez ces modifications (*git add* et *git
commit -m "..."*).
*Fait.*

5. Familiarisez vous avec le contenu du répertoire, qui devrait
ressembler à :

```
├── README.md
├── img
│   └── test_1.png
├── src
│   ├── fonctions_test.py
│   ├── quadratures.py
│   └── tests.py
└── tex
    ├── memo_quadratures.pdf
    ├── memo_quadratures.tex
```

Quel est la nature (langage ?) et le rôle (texte, programme, autre) de
chacun des fichiers présents ?
*Le fichier "README.md" est un fichier Markdown de GIT.
Les fichiers .png sont des images.
Les fichiers .py sont des fichiers code Python.
Le fichier .tex est écrit en Latex.
Le fichier .pdf est le fichier .tex compilé.*

**Pensez à valider régulièrement votre travail, et à pousser les
  changements sur le serveur (*git push*)**

## Deuxième partie: formules de quadrature

1. En suivant le modèle de la formule du point milieu, dans le fichier
[./src/quadratures.py](./src/quadratures.py) programmer la méthode des
trapèzes (programmer une autre fonction dans le même fichier
[./src/quadratures.py](./src/quadratures.py)).
*Fait.*

2. Tester cette nouvelle quadrature en utilisant comme modèle le
programme [./src/tests.py](./src/tests.py): vérifier que cette formule
calcul de manière exacte les intégrales de polynômes de degré au plus 1,
et comment une erreur équivalente à $h^2$ (ou encore
$N^{-2}$). Reproduire ci-dessous les tableaux d'erreurs qui démontrent
ce résultat, et inclure le graphe de convergence des approximations.

### Méthode : Trapèzes
#### Test pour le monôme de degré 0

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 2 | 2 | 0
2 | 2 | 2 | 0
4 | 2 | 2 | 0
8 | 2 | 2 | 0
16 | 2 | 2 | 0
32 | 2 | 2 | 0
64 | 2 | 2 | 0
128 | 2 | 2 | 0
256 | 2 | 2 | 0
512 | 2 | 2 | 0
1024 | 2 | 2 | 0
2048 | 2 | 2 | 0
4096 | 2 | 2 | 0
8192 | 2 | 2 | 0
16384 | 2 | 2 | 0
32768 | 2 | 2 | 0
65536 | 2 | 2 | 0
131072 | 2 | 2 | 0
262144 | 2 | 2 | 0
524288 | 2 | 2 | 0

Ordre de convergence moyen : nan

On remarque les erreurs en valeurs absolues commises entre la solution analytique et la solution numérique sont nulles. Cela signifie que pour N et donc pour tout h pas d'espace, la méthode des trapèzes intègre parfaitement le monôme de degré 0 et donc tous les polynômes de degré 0 (les polynômes constants). L´ordre de convergence moyen n'a donc pas de sens puisque cette méthode d'intégration est exacte.


#### Test pour le monôme de degré 1

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0 | 0 | 0
2 | 0 | 0 | 0
4 | 0 | 0 | 0
8 | 0 | 0 | 0
16 | 0 | 0 | 0
32 | 0 | 0 | 0
64 | 0 | 0 | 0
128 | 0 | 0 | 0
256 | 0 | 0 | 0
512 | 0 | 0 | 0
1024 | 0 | 0 | 0
2048 | 0 | 0 | 0
4096 | 0 | 0 | 0
8192 | 0 | 0 | 0
16384 | 0 | 0 | 0
32768 | 0 | 0 | 0
65536 | 0 | 0 | 0
131072 | 0 | 0 | 0
262144 | 0 | 0 | 0
524288 | 0 | 0 | 0

Ordre de convergence moyen : nan

On remarque les erreurs en valeurs absolues commises entre la solution analytique et la solution numérique sont nulles. Cela signifie que pour N et donc pour tout h pas d'espace, la méthode des trapèzes intègre parfaitement le monôme de degré 1 et donc tous les polynômes de degré 1 (les polynômes ax+b avec a et b réels). L´ordre de convergence moyen n'a donc pas de sens puisque cette méthode d'intégration est exacte.

#### Test pour le monome de degré 2

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0.666667 | 2 | 1.33333
2 | 0.666667 | 1 | 0.333333
4 | 0.666667 | 0.75 | 0.0833333
8 | 0.666667 | 0.6875 | 0.0208333
16 | 0.666667 | 0.671875 | 0.00520833
32 | 0.666667 | 0.667969 | 0.00130208
64 | 0.666667 | 0.666992 | 0.000325521
128 | 0.666667 | 0.666748 | 8.13802e-05
256 | 0.666667 | 0.666687 | 2.03451e-05
512 | 0.666667 | 0.666672 | 5.08626e-06
1024 | 0.666667 | 0.666668 | 1.27157e-06
2048 | 0.666667 | 0.666667 | 3.17891e-07
4096 | 0.666667 | 0.666667 | 7.94729e-08
8192 | 0.666667 | 0.666667 | 1.98682e-08
16384 | 0.666667 | 0.666667 | 4.96705e-09
32768 | 0.666667 | 0.666667 | 1.24176e-09
65536 | 0.666667 | 0.666667 | 3.10441e-10
131072 | 0.666667 | 0.666667 | 7.76103e-11
262144 | 0.666667 | 0.666667 | 1.94026e-11
524288 | 0.666667 | 0.666667 | 4.85068e-12

Ordre de convergence moyen : 1.9999994206922278

Par rapport aux deux cas précédents, on peut constater que les erreurs commises ne sont pas nulles, donc la méthode des trapèzes n’intègre pas parfaitement les monômes de degré 2, et donc a fortiori les polynômes ax^2+bx+c avec a,b, et c réels.
À côté de cela, on constate que l'erreur commise est divisée par 4 lorsque le pas h est divisé par 2 : l'ordre de convergence de la méthode est donc de 2.


#### Test pour le monôme de degré 3

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0 | 0 | 0
2 | 0 | 0 | 0
4 | 0 | 0 | 0
8 | 0 | 0 | 0
16 | 0 | 0 | 0
32 | 0 | 0 | 0
64 | 0 | 0 | 0
128 | 0 | 0 | 0
256 | 0 | 0 | 0
512 | 0 | 0 | 0
1024 | 0 | 0 | 0
2048 | 0 | 0 | 0
4096 | 0 | 0 | 0
8192 | 0 | 0 | 0
16384 | 0 | 0 | 0
32768 | 0 | 0 | 0
65536 | 0 | 0 | 0
131072 | 0 | 0 | 0
262144 | 0 | 0 | 0
524288 | 0 | 0 | 0

Ordre de convergence moyen : nan

Cas particulier : sur l'intervalle [-1, 1] la fonction est symétrique et l'intégrale vaut 0.


#### Test pour le monôme de degré 4

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0.4 | 2 | 1.6
2 | 0.4 | 1 | 0.6
4 | 0.4 | 0.5625 | 0.1625
8 | 0.4 | 0.441406 | 0.0414062
16 | 0.4 | 0.4104 | 0.0104004
32 | 0.4 | 0.402603 | 0.00260315
64 | 0.4 | 0.400651 | 0.000650978
128 | 0.4 | 0.400163 | 0.000162756
256 | 0.4 | 0.400041 | 4.06899e-05
512 | 0.4 | 0.40001 | 1.01725e-05
1024 | 0.4 | 0.400003 | 2.54313e-06
2048 | 0.4 | 0.400001 | 6.35783e-07
4096 | 0.4 | 0.4 | 1.58946e-07
8192 | 0.4 | 0.4 | 3.97364e-08
16384 | 0.4 | 0.4 | 9.93411e-09
32768 | 0.4 | 0.4 | 2.48353e-09
65536 | 0.4 | 0.4 | 6.20882e-10
131072 | 0.4 | 0.4 | 1.55221e-10
262144 | 0.4 | 0.4 | 3.88049e-11
524288 | 0.4 | 0.4 | 9.70107e-12

Ordre de convergence moyen : 1.9612139302683098


#### Test pour le monôme de degré 5

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0 | 0 | 0
2 | 0 | 0 | 0
4 | 0 | 0 | 0
8 | 0 | 0 | 0
16 | 0 | 0 | 0
32 | 0 | 0 | 0
64 | 0 | 0 | 0
128 | 0 | 0 | 0
256 | 0 | 0 | 0
512 | 0 | 0 | 0
1024 | 0 | 0 | 0
2048 | 0 | 0 | 0
4096 | 0 | 0 | 0
8192 | 0 | 0 | 0
16384 | 0 | 0 | 0
32768 | 0 | 0 | 0
65536 | 0 | 0 | 0
131072 | 0 | 1.38778e-17 | 1.38778e-17
262144 | 0 | -1.38778e-17 | 1.38778e-17
524288 | 0 | 3.1225e-17 | 3.1225e-17

Ordre de convergence moyen : nan

Cas particulier : sur l'intervalle [-1, 1] la fonction est symétrique et l'intégrale vaut 0.
Le *e-17* dénote juste une erreur d'arrondi machine.


#### Test pour le monôme de degré 6

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 0.285714 | 2 | 1.71429
2 | 0.285714 | 1 | 0.714286
4 | 0.285714 | 0.515625 | 0.229911
8 | 0.285714 | 0.346924 | 0.0612095
16 | 0.285714 | 0.301258 | 0.0155438
32 | 0.285714 | 0.289615 | 0.00390117
64 | 0.285714 | 0.286691 | 0.000976245
128 | 0.285714 | 0.285958 | 0.000244121
256 | 0.285714 | 0.285775 | 6.10339e-05
512 | 0.285714 | 0.28573 | 1.52587e-05
1024 | 0.285714 | 0.285718 | 3.81469e-06
2048 | 0.285714 | 0.285715 | 9.53674e-07
4096 | 0.285714 | 0.285715 | 2.38419e-07
8192 | 0.285714 | 0.285714 | 5.96046e-08
16384 | 0.285714 | 0.285714 | 1.49012e-08
32768 | 0.285714 | 0.285714 | 3.72529e-09
65536 | 0.285714 | 0.285714 | 9.31323e-10
131072 | 0.285714 | 0.285714 | 2.32831e-10
262144 | 0.285714 | 0.285714 | 5.82075e-11
524288 | 0.285714 | 0.285714 | 1.4552e-11

Ordre de convergence moyen : 1.935662977463994

![Tests monomes trapeze](/img/test_monomes_trapeze.png)

3. On veut tester nos formules pour d'autres fonctions que les
polynômes. Pour cela, on ajoute les fonctions souhaitées dans le fichier
[./src/fonctions_test.py](./src/fonctions_test.py). En suivant le modèle
donné pour les monômes, programmer les fonctions (et une de leurs
primitives)
 - $f(x) = |x|$ et $g(x) = 0.5*x*|x|$;
 - $f(x) = cos(x)$ et $g(x) = sin(x)$;
 - $f(x) = exp(x)$ et $g(x) = exp(x)$;
 - $f(x) = 1/(1+x^2)$ et $g(x) = atan(x)$.

*Fait.
Ajout de la fonction absWith(x) = abs(x - pi/10).*

4. En adaptant le programme [./src/tests.py](./src/tests.py), produire
une unique figure qui compare les graphes de convergence de l'erreur
pour ces nouvelles fonctions intégrées sur l'intervalle
$[-1,1]$. Insérez l'image ci-dessous, et faites tous les commentaires
utiles.

![Tests fonctions trapèze](/img/test_fonction_trapeze.png)

La fonction abs étant linéaire est symétrique par rapport à x = 0 donc sur l'intervalle [-1, 1], elle est intégrée parfaitement dès N = 2 car la méthode des trapèzes est exactes pour les polynômes de degré 1 et dès N=2 l'un des points d'intégration est situé sur le point x = 0.
Contrairement à la fonction absWith (x) = abs (x - pi/10) qui est définie sur un translation de la fonction abs sur un intervalle non rationnel : le point d'intégration x = - pi / 10 n'existe pas !
L'ordre de convergence de la méthode semble bien être 2 comme ce qui était explicité dans la question précédente.

Pour plus de précision, donnez un tableau comparatif des erreurs commise
pour la méthode du point milieu pour chacune des ces fonctions.

#### Test pour f(x) = absWith(x)
##### Point milieu


N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.0987 | 0.628319 | 0.470378
2 | 1.0987 | 1 | 0.098696
4 | 1.0987 | 1.06416 | 0.0345368
8 | 1.0987 | 1.09458 | 0.00411641
16 | 1.0987 | 1.09499 | 0.00370159
32 | 1.0987 | 1.09869 | 2.75316e-06
64 | 1.0987 | 1.09869 | 2.75316e-06
128 | 1.0987 | 1.09869 | 2.75316e-06
256 | 1.0987 | 1.09869 | 2.75316e-06
512 | 1.0987 | 1.09869 | 2.75316e-06
1024 | 1.0987 | 1.0987 | 8.63535e-08
2048 | 1.0987 | 1.0987 | 8.63535e-08
4096 | 1.0987 | 1.0987 | 3.77998e-08
8192 | 1.0987 | 1.0987 | 2.47198e-09
16384 | 1.0987 | 1.0987 | 2.47198e-09
32768 | 1.0987 | 1.0987 | 1.28055e-10
65536 | 1.0987 | 1.0987 | 1.28055e-10
131072 | 1.0987 | 1.0987 | 1.55442e-11
262144 | 1.0987 | 1.0987 | 1.35922e-11
524288 | 1.0987 | 1.0987 | 1.59872e-14

Ordre de convergence moyen : 2.3548403156055655



#### Trapèzes

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.0987 | 2 | 0.901304
2 | 1.0987 | 1.31416 | 0.215463
4 | 1.0987 | 1.15708 | 0.0583836
8 | 1.0987 | 1.11062 | 0.0119234
16 | 1.0987 | 1.1026 | 0.0039035
32 | 1.0987 | 1.0988 | 0.000100951
64 | 1.0987 | 1.09875 | 4.90989e-05
128 | 1.0987 | 1.09872 | 2.31729e-05
256 | 1.0987 | 1.09871 | 1.02098e-05
512 | 1.0987 | 1.0987 | 3.72834e-06
1024 | 1.0987 | 1.0987 | 4.87591e-07
2048 | 1.0987 | 1.0987 | 2.00619e-07
4096 | 1.0987 | 1.0987 | 5.71327e-08
8192 | 1.0987 | 1.0987 | 9.66645e-09
16384 | 1.0987 | 1.0987 | 3.59724e-09
32768 | 1.0987 | 1.0987 | 5.62628e-10
65536 | 1.0987 | 1.0987 | 2.17286e-10
131072 | 1.0987 | 1.0987 | 4.46156e-11
262144 | 1.0987 | 1.0987 | 1.45355e-11
524288 | 1.0987 | 1.0987 | 4.72067e-13

Ordre de convergence moyen : 2.1471663024496266

#### Test pour f(x) = abs(x)
##### Point milieu

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1 | 0 | 1
2 | 1 | 1 | 0
4 | 1 | 1 | 0
8 | 1 | 1 | 0
16 | 1 | 1 | 0
32 | 1 | 1 | 0
64 | 1 | 1 | 0
128 | 1 | 1 | 0
256 | 1 | 1 | 0
512 | 1 | 1 | 0
1024 | 1 | 1 | 0
2048 | 1 | 1 | 0
4096 | 1 | 1 | 0
8192 | 1 | 1 | 0
16384 | 1 | 1 | 0
32768 | 1 | 1 | 0
65536 | 1 | 1 | 0
131072 | 1 | 1 | 0
262144 | 1 | 1 | 0
524288 | 1 | 1 | 0

Ordre de convergence moyen : nan


#### Trapèzes

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1 | 2 | 1
2 | 1 | 1 | 0
4 | 1 | 1 | 0
8 | 1 | 1 | 0
16 | 1 | 1 | 0
32 | 1 | 1 | 0
64 | 1 | 1 | 0
128 | 1 | 1 | 0
256 | 1 | 1 | 0
512 | 1 | 1 | 0
1024 | 1 | 1 | 0
2048 | 1 | 1 | 0
4096 | 1 | 1 | 0
8192 | 1 | 1 | 0
16384 | 1 | 1 | 0
32768 | 1 | 1 | 0
65536 | 1 | 1 | 0
131072 | 1 | 1 | 0
262144 | 1 | 1 | 0
524288 | 1 | 1 | 0

Ordre de convergence moyen : nan


#### Test pour f(x) = exp(x)
##### Point milieu

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 2.3504 | 2 | 0.350402
2 | 2.3504 | 2.25525 | 0.0951505
4 | 2.3504 | 2.3261 | 0.024306
8 | 2.3504 | 2.34429 | 0.0061097
16 | 2.3504 | 2.34887 | 0.00152951
32 | 2.3504 | 2.35002 | 0.000382509
64 | 2.3504 | 2.35031 | 9.56354e-05
128 | 2.3504 | 2.35038 | 2.39094e-05
256 | 2.3504 | 2.3504 | 5.97737e-06
512 | 2.3504 | 2.3504 | 1.49434e-06
1024 | 2.3504 | 2.3504 | 3.73586e-07
2048 | 2.3504 | 2.3504 | 9.33966e-08
4096 | 2.3504 | 2.3504 | 2.33491e-08
8192 | 2.3504 | 2.3504 | 5.83729e-09
16384 | 2.3504 | 2.3504 | 1.45932e-09
32768 | 2.3504 | 2.3504 | 3.6483e-10
65536 | 2.3504 | 2.3504 | 9.12075e-11
131072 | 2.3504 | 2.3504 | 2.28018e-11
262144 | 2.3504 | 2.3504 | 5.70033e-12
524288 | 2.3504 | 2.3504 | 1.42419e-12

Ordre de convergence moyen : 1.99158294056363


#### Trapèzes
N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 2.3504 | 3.08616 | 0.735759
2 | 2.3504 | 2.54308 | 0.192678
4 | 2.3504 | 2.39917 | 0.0487639
8 | 2.3504 | 2.36263 | 0.0122289
16 | 2.3504 | 2.35346 | 0.00305962
32 | 2.3504 | 2.35117 | 0.000765055
64 | 2.3504 | 2.35059 | 0.000191273
128 | 2.3504 | 2.35045 | 4.78189e-05
256 | 2.3504 | 2.35041 | 1.19548e-05
512 | 2.3504 | 2.35041 | 2.98869e-06
1024 | 2.3504 | 2.3504 | 7.47173e-07
2048 | 2.3504 | 2.3504 | 1.86793e-07
4096 | 2.3504 | 2.3504 | 4.66983e-08
8192 | 2.3504 | 2.3504 | 1.16746e-08
16384 | 2.3504 | 2.3504 | 2.91864e-09
32768 | 2.3504 | 2.3504 | 7.29661e-10
65536 | 2.3504 | 2.3504 | 1.82415e-10
131072 | 2.3504 | 2.3504 | 4.5604e-11
262144 | 2.3504 | 2.3504 | 1.14007e-11
524288 | 2.3504 | 2.3504 | 2.8515e-12

Ordre de convergence moyen : 1.9951959303024893




#### Test pour f(x) = cos(x)
##### Point milieu

N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.68294 | 2 | 0.317058
2 | 1.68294 | 1.75517 | 0.0722232
4 | 1.68294 | 1.7006 | 0.0176593
8 | 1.68294 | 1.68733 | 0.00439066
16 | 1.68294 | 1.68404 | 0.00109616
32 | 1.68294 | 1.68322 | 0.000273948
64 | 1.68294 | 1.68301 | 6.8481e-05
128 | 1.68294 | 1.68296 | 1.71199e-05
256 | 1.68294 | 1.68295 | 4.27995e-06
512 | 1.68294 | 1.68294 | 1.06999e-06
1024 | 1.68294 | 1.68294 | 2.67496e-07
2048 | 1.68294 | 1.68294 | 6.68741e-08
4096 | 1.68294 | 1.68294 | 1.67185e-08
8192 | 1.68294 | 1.68294 | 4.17963e-09
16384 | 1.68294 | 1.68294 | 1.04491e-09
32768 | 1.68294 | 1.68294 | 2.61227e-10
65536 | 1.68294 | 1.68294 | 6.53069e-11
131072 | 1.68294 | 1.68294 | 1.63269e-11
262144 | 1.68294 | 1.68294 | 4.08162e-12
524288 | 1.68294 | 1.68294 | 1.02052e-12

Ordre de convergence moyen : 2.0092976705301333


##### Trapèzes
N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.68294 | 1.0806 | 0.602337
2 | 1.68294 | 1.5403 | 0.14264
4 | 1.68294 | 1.64773 | 0.0352083
8 | 1.68294 | 1.67417 | 0.00877447
16 | 1.68294 | 1.68075 | 0.0021919
32 | 1.68294 | 1.68239 | 0.000547868
64 | 1.68294 | 1.68281 | 0.00013696
128 | 1.68294 | 1.68291 | 3.42397e-05
256 | 1.68294 | 1.68293 | 8.55989e-06
512 | 1.68294 | 1.68294 | 2.13997e-06
1024 | 1.68294 | 1.68294 | 5.34993e-07
2048 | 1.68294 | 1.68294 | 1.33748e-07
4096 | 1.68294 | 1.68294 | 3.34371e-08
8192 | 1.68294 | 1.68294 | 8.35926e-09
16384 | 1.68294 | 1.68294 | 2.08982e-09
32768 | 1.68294 | 1.68294 | 5.22454e-10
65536 | 1.68294 | 1.68294 | 1.30613e-10
131072 | 1.68294 | 1.68294 | 3.26534e-11
262144 | 1.68294 | 1.68294 | 8.1628e-12
524288 | 1.68294 | 1.68294 | 2.04126e-12

Ordre de convergence moyen : 2.0053854536675395


#### Test pour f(x) = arctan_der(x)
##### Point milieu
N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.5708 | 2 | 0.429204
2 | 1.5708 | 1.6 | 0.0292037
4 | 1.5708 | 1.58118 | 0.0103801
8 | 1.5708 | 1.5734 | 0.00260393
16 | 1.5708 | 1.57145 | 0.000651038
32 | 1.5708 | 1.57096 | 0.00016276
64 | 1.5708 | 1.57084 | 4.06901e-05
128 | 1.5708 | 1.57081 | 1.01725e-05
256 | 1.5708 | 1.5708 | 2.54313e-06
512 | 1.5708 | 1.5708 | 6.35783e-07
1024 | 1.5708 | 1.5708 | 1.58946e-07
2048 | 1.5708 | 1.5708 | 3.97364e-08
4096 | 1.5708 | 1.5708 | 9.93411e-09
8192 | 1.5708 | 1.5708 | 2.48353e-09
16384 | 1.5708 | 1.5708 | 6.20882e-10
32768 | 1.5708 | 1.5708 | 1.55221e-10
65536 | 1.5708 | 1.5708 | 3.88052e-11
131072 | 1.5708 | 1.5708 | 9.70113e-12
262144 | 1.5708 | 1.5708 | 2.42539e-12
524288 | 1.5708 | 1.5708 | 6.0596e-13

Ordre de convergence moyen : 2.0718725078336346


##### Trapèzes
N[i]  |       I        |      Q[i]      |      E[i]     
----- | -------------- | -------------- | --------------
1 | 1.5708 | 1 | 0.570796
2 | 1.5708 | 1.5 | 0.0707963
4 | 1.5708 | 1.55 | 0.0207963
8 | 1.5708 | 1.56559 | 0.00520809
16 | 1.5708 | 1.56949 | 0.00130208
32 | 1.5708 | 1.57047 | 0.000325521
64 | 1.5708 | 1.57071 | 8.13802e-05
128 | 1.5708 | 1.57078 | 2.03451e-05
256 | 1.5708 | 1.57079 | 5.08626e-06
512 | 1.5708 | 1.5708 | 1.27157e-06
1024 | 1.5708 | 1.5708 | 3.17891e-07
2048 | 1.5708 | 1.5708 | 7.94729e-08
4096 | 1.5708 | 1.5708 | 1.98682e-08
8192 | 1.5708 | 1.5708 | 4.96705e-09
16384 | 1.5708 | 1.5708 | 1.24176e-09
32768 | 1.5708 | 1.5708 | 3.10441e-10
65536 | 1.5708 | 1.5708 | 7.76101e-11
131072 | 1.5708 | 1.5708 | 1.94027e-11
262144 | 1.5708 | 1.5708 | 4.85079e-12
524288 | 1.5708 | 1.5708 | 1.21236e-12

Ordre de convergence moyen : 2.04086119579347


5. Programmez maintenant la méthode de Simpson et les méthodes de
   Gauss-Legendre à 2 et 3 points (voir le document
   [./tex/memo_quadratures.pdf](./tex/memo_quadratures.pdf)). Expliquez
   la stratégie de programmation retenue. Vérifiez numériquement que les
   formules intègrent exactement les polynômes de degré au plus 3
   (Simpson, Gauss-Legendre à 2 points) ou 5 (Gauss-Legendre à 3
   points). Calculez numériquement l'ordre de convergence de ces
   méthodes.
   *Fait.*
   Pour la partie "programmation des méthodes", j'ai préféré séparer les différentes méthodes. On aurait très bien pu utiliser un tableau de poids et de point d'intégration : cela aurait allégé la méthode et la programmation mais alourdi l'utilisation des méthodes en tant que fonction utilisée par l'utilisateur je trouve. Mais cela reste possible, et cela est encore plus judicieux si d'autres méthodes doivent être programmées (Formules de Newton-Côtes).
   Les ordres de convergence ont été établi numériquement dans les questions précédentes.
   Pour rappel :

   - Point-Milieu : 2,
   - Trapèzes : 2,
   - Simpson : 4,
   - Gauss-Legendre à 2 points : 1 ou 2 suivant la fonction,
   - Gauss-Legendre à 3 points : 1 ou 2 suivant la fonction.

   ![Tests pt_milieu](/img/test_pt_milieu.png)
   ![Tests trapeze](/img/test_trapezes.png)
   ![Tests simpson](/img/test_simpson.png)
   ![Tests gauss_legendre_2](/img/test_gauss_legendre_2pts.png)
   ![Tests gauss_legendre_3](/img/test_gauss_legendre_3pts.png)

   J'ai fait aussi le choix de programmer les méthodes de quadratures de Gauss-Legendre à 1, 2, 3, 4, 5 points tels que trouvées sur Wikipedia.
   J'ai trouvé des résultats complètement différents par rapport aux formules employées précédemment :
   J'ai du rentrer en dur les valeurs des points et des poids avec 30 chiffres significatifs car les erreurs d'arrondis machines étaient trop présents, ceci empêchant l'erreur de descendre en bas de des 10**(-15).

   Ordre de convergence :
   - Gauss-Legendre à 1 points : 2
   - Gauss-Legendre à 2 points : 2 (absWith), 4 ou 6 suivant la fonction
   - Gauss-Legendre à 3 points : 6
   - Gauss-Legendre à 4 points : 2 (absWith), 8, 11 suivant la fonction
   - Gauss-Legendre à 5 points : 2 (absWith), 10, 12 suivant la fonction

   ![Tests gauss_legendre_1](/img/test_gauss_legendre_1pts_other.png)
   ![Tests gauss_legendre_2](/img/test_gauss_legendre_2pts_other.png)
   ![Tests gauss_legendre_3](/img/test_gauss_legendre_3pts_other.png)
   ![Tests gauss_legendre_4](/img/test_gauss_legendre_4pts_other.png)
   ![Tests gauss_legendre_5](/img/test_gauss_legendre_5pts_other.png)



6. On peut maintenant comparer la précision et la vitesse de convergence
   de ces 3 méthodes supplémentaires avec la méthode du point
   milieu. Pour cela, dressez un tableau et un graphe de convergence
   pour chacune des fonctions de la question 3. Vous pouvez discuter du
   résultat.
   *Fait.*
   J'ai incorporé tous les graphes possibles mais je n'analyserai que la seconde vague (avec les quadratures de Gauss-Legendre recodées).

   ### Méthodes du PDF
   ![Tests x**0](/img/test_x0.png)
   ![Tests x**1](/img/test_x1.png)
   ![Tests x**2](/img/test_x2.png)
   ![Tests x**3](/img/test_x3.png)
   ![Tests x**4](/img/test_x4.png)
   ![Tests x**5](/img/test_x5.png)
   ![Tests x**6](/img/test_x6.png)
   ![Tests abs](/img/test_abs.png)
   ![Tests absWith](/img/test_absWith.png)
   ![Tests cos](/img/test_cos.png)
   ![Tests exp](/img/test_exp.png)
   ![Tests arctan_der](/img/test_arctan_der.png)


   ### Méthodes online

   ![Tests x**0](/img/test_x0_other.png)

   Le monôme x**0 est intégré parfaitement par toutes les méthodes, et donc a fortiori toutes les fonctions constantes sur [-1, 1].

   ![Tests x**1](/img/test_x1_other.png)

  Le monôme x**1 est intégré parfaitement par toutes les méthodes, et donc a fortiori toutes les fonctions pouvant s'écrire ax+b sur [-1, 1].

   ![Tests x**2](/img/test_x2_other.png)

    Le monôme x**2 est intégré parfaitement par toutes les méthodes sauf la méthodes des trapèzes et de Gauss-Legendre à 1 point.

   ![Tests x**3](/img/test_x3_other.png)

   Le monôme x**3 est intégré parfaitement par toutes les méthodes car cette fonction est symétrique sur [-1, 1] et l'intégrale vaut 0.

   ![Tests x**4](/img/test_x4_other.png)

   Le monômes x**4 est uniquement intégré parfaitement  par les méthodes de Gauss-Legendre à 3, 4, et 5 points.

   ![Tests x**5](/img/test_x5_other.png)

  Le monôme x**5 est intégré parfaitement par toutes les méthodes car cette fonction est symétrique sur [-1, 1] et l'intégrale vaut 0.

   ![Tests x**6](/img/test_x6_other.png)

   Le monômes x**6 est uniquement intégré parfaitement  par les méthodes de Gauss-Legendre à 4, et 5 points.
   
   ![Tests abs](/img/test_abs_other.png)

   La fonction abs est intégrée parfaitement par toutes les méthodes car cette fonction est symétrique en x = 0 sur [-1, 1] et est affine par morceaux autour du point de symétrie.

   ![Tests absWith](/img/test_absWith_other.png)

   La fonction absWith(x) = abs (x - pi / 10) n'est intégrée parfaitement par aucune méthode à cause du point de symétrie non-rationnel en x = -pi / 10. L'ordre de convergence pour touts les méthodes est globalement  de 2.

   ![Tests cos](/img/test_cos_other.png)

   La fonction cosinus est intégrée avec différents ordre de convergence selon les méthodes.

   ![Tests exp](/img/test_exp_other.png)

   La fonction exp est intégrée avec différents ordre de convergence selon les méthodes.

   ![Tests arctan_der](/img/test_arctan_der_other.png)

   La dérivée de l’arc-tangente est intégrée avec différents ordre de convergence selon les méthodes.


  ### Classement des méthodes selon leur ordre de convergence

  1. Gauss-Legendre à 5 points (o.c : 10)
  2. Gauss-Legendre à 4 points (o.c : 8)
  3. Gauss-Legendre à 3 points (o.c : 6)
  4. Gauss-Legendre à 2 points (o.c : 4)
  5. Simpson (o.c : 4)
  6. Gauss-Legendre à 1 point (o.c : 2)
  7. Trapèzes (o.c : 2)
  8. Point-milieu (o.c : 2)


**N'oubliez pas de valider les modifications faites le plus souvent
possible (*validations atomiques*), et de documenter intelligiblement
l'historique associé (les messages). Finalement, n'oubliez pas de
pousser votre travail sur le dépôt.**
