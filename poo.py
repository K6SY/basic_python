class Personne():
    #Définition du constructeur (méthode spéciale appelé à la création de l'objet)
    def __init__(self):
        self.nom = "default_nom"
        self.prenom = "default_prenom"
    
    def setNom(self,nom):
        try:
            if nom.isalpha():
                self.nom = nom
        except AttributeError:
            print("Modification impossible")
    
    def getNom(self):
        return self.nom
    
    def setPrenom(self,prenom):
        self.prenom = prenom

    def getPrenom(self):
        return self.prenom

    #Fonctions spécifiques permettant de formater un objet
    def __str__(self):
        return f"Nom: {self.nom} - Prenoms: {self.prenom}"
    
class Filiere():
    pass

p1 = Personne()
p2 = Personne()

f1 = Filiere()
f2 = Filiere()

p2.setNom(12)
p2.nom=12
print(p2.nom)
'''
print("Avant modification: ",p1)

nom = input("Entrer le nom de la personne")
p1.setNom(nom)

print("Après modification",p1)
'''