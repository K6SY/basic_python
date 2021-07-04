'''
    Fonctions built-ins: Les fonctions prédéfinies dans le  noyau (ex: print, input)

    Bibliothèques : extension de code dépendant d'un domaine et qui permet la réutilisation de code
        * 1er lot: inclus dans l'installation par défaut
            - math : Qui offre des fonctionnalités (fonctions, classe, module, package, constantes, etc. )pour faire des maths dans IR
            - datetime: Qui permet de manipuler les dates en python
            - random: qui offre des fonctions & constante pour générer des nombres aléatoires
            - cmath: Qui offre des fonctionnalités (fonctions, classe, module, package, constantes, etc. )pour faire des maths dans IC
            - os: qui offre des fonctionnalités (fonctions, classe, module, package, constantes, etc. )permettant de gérer les systèmes de fichiers
            - tkinter: qui offre des fonctionnalités (fonctions, classe, module, package, constantes, etc. )pour le développement d'interface graphique
            - etc.
        * 2e lot: requiert l'installation d'un package (via l'utilitaire pip)
            - flask : permet de faire du développement web
            - mysql-connector-python: permet de faire des opérations sur une base MySQL ou Mariadb
            - scikit-learn: Permet de faire du Machine Learning avec Python
            - OpenCV: permet de faire du traitement d'image / vidéo (ML) avec Python
            - Numpy: permet de faire des calculs numériques
            - Scipy: permet de faire des calculs scientifiques
            - etc.

        ToDo:
            - importation de la bibliothèque
            - Utilisation des fonctionnalités (fonctions, classe, module, package, constantes, etc. )de la bibliothèque

'''

#1ère technique d'importation
#Syntaxe: import nom_bibliotheque
import math
import cmath
import common


#2eme technique d'importation
#Syntaxe: from nom_bibliotheque import element
from datetime import datetime
from random import *

#from cmath import sqrt as sc
#from math import sqrt as sr, pow, ceil, floor


#Utilisation avec 1ere technique d'importation
racine_r = math.sqrt(25)
racine_c = cmath.sqrt(-25)

print(f"Racine de 25 dans IR : {racine_r}")
print(f"Racine de -25 dans IC : {racine_c}")

#Utilisation avec 2ere technique d'importation
choix=randint(1,67)
print(f"Nombre généré: {choix}")

datenow = datetime.now()
print(f"Date et heure execution: {datenow}")
#Utilisation avec 2ere technique d'importation avec usage alias
#racine_r = sr(25)
#racine_c = sc(-25)
#print(f"Racine de 25 dans IR : {racine_r}")
#print(f"Racine de -25 dans IC : {racine_c}")

