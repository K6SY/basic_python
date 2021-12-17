'''
    (*) Module: fichier python contenant des fonctions et des constantes

    (*) Package: répertoire contenant des fichiers python avec un fichier spécifique 
    nommé __init__.py


    Etudiant 1 : Trousseau (clé usb, stylos, gomme, blanco)

    Etudiant 2 : Trousseau (clé usb, stylos, gomme, taille, rapport, compas)

    Use case 1: Etudiant 3 veut emprunter une clé à l'étudiant 1
        - Appeler Etudiant
        - Emprunter la clé

    use case2: façon de remettre la clé à l'étudiant 3
        - Ouvrir le trousseau et remettre la clé
        - Donner le trousseau et l'étudiant 3 prend la clé

'''
#Importer tout le module
import os.path

#importer une fonction sur le module
from math import sqrt
from random import randint

'''
    1e méthode importation ---> import module
    module.fonction()
'''
'''
    2e méthode importation ---> from module import fonction
    usage: fonction()
'''

''' 
    A éviter

    - import module ---> fonction()
    - from module import fonction ----> module.fonction()



a = sqrt(25)
print(a)

