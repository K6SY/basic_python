from datetime import datetime

class Categorie:

    def __init__(self,nom,description=None):
        self.__nom = nom
        self.__description = description
        self.__produit=[]

    def getNom(self):
        return self.__nom
    
    def getDescription(self):
        return self.__description
    
    def getProduit(self):
        return self.__produit


class Produit:
    def __init__(self,nom,prix,description=None, categorie=None):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.categorie = categorie

class Stock:

    def __init__(self,produit,quantite, commentaire=None):
        self.produit = produit
        self.quantite = quantite
        self.commentaire = commentaire
        self.dateCreatio = datetime.now()