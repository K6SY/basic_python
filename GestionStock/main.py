from classes import Categorie, Produit, Stock
from common import *
boutique = {}
continuer=True
affichageTitre("Bienvenue dans GeStock",30)
while continuer:
    print('''
        - Taper 1 pour gérer une categorie
        - Taper 2 pour gérer un produit
        - Taper 3  pour gérer votre stock
        - taper tout autre touche pour quitter
    ''')
    choix=input()
    if not choix.isdigit():
        continuer=False
    else:
        while int(choix) not in (1,2,3):
            print('Veuillez effectuer un bon choix')
            choix=input()
        choix=int(choix)
        if choix == 1:
            affichageTitre('Categorie',10)
            choix1 = menuCategorie()
            if choix1 == 1:
                c1=createCategorie()
                boutique[c1.getNom()]=c1

        elif choix1 == 2:
            affichageTitre('Produit',10)
        else:
            affichageTitre('Stock',10)
    
    print(boutique)
