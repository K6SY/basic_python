'''

    Classe: Représentation abstraite 
        - Caractéristiques --> attribut / propriété (variable )
        - méthodes (actions) --> fonctions ()

    objet: instance de la classe (concret)

    Device:

        - Marque: Mac OS
        - Processor: 2,2 GHz 6-Core Intel Core i7
        - version os: Mac Big SUR
        - RAM: 16Go

        - Marque: Asus
        - Processor : Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz  1.20 GHz
        - version os: Windows 11

        - Marque: Thinkpad X230
        - version os: Kubuntu (Linux)
        - Processor : 2.6
'''


#Création de classe

class Patient():
    #Constructeur
    def __init__(self,nom,prenom,sexe,adresse="NA",age=0):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.age = age
        self.sexe=sexe

    def updateAdresse(self,adresse):
        self.adresse = adresse

class Medecin():
    pass

class Consultation():
    pass

#Instanciation
p1 = Patient('Ndiaye','Aliou','M')
p2 = Patient('Ndiaye','Aliou','M',adresse="Medina",age=32)

print(p1.adresse)

p1.updateAdresse('Niaye Tiocker')

print(p1.adresse)