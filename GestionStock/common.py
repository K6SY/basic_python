from classes import Categorie
def affichageTitre(message, longueur):
    print('-'*longueur)
    print(message.center(longueur))
    print('-'*longueur)

def menuCategorie():
    while True:
        print('''
            - Taper 1 pour créer une categorie
            - Taper 2 pour afficher une categorie
            - Taper 3  pour lister les categories
            - taper tout autre touche pour quitter
        ''')
        choix=input()
        if not choix.isdigit():
            choix=-1
            break
        else:
            while int(choix) not in (1,2,3):
                print('Veuillez effectuer un bon choix')
                choix=input()
            choix=int(choix)
            break
    
    return choix

def createCategorie():
    nom=input("indiquer le nom de la catégorie")
    description=input("indiquer la description de la catégorie")
    cat = Categorie(nom,description)
    return cat