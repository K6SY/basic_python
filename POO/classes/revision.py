
class Ecole:

    #Constructeur

    @classmethod
    def getEmplacement(cls):
        print("Les écoles au SENEGAL")

    def __init__(self, nom, adresse="", slogan=""):
        self.__nom = nom
        self.adresse = adresse
        self.slogan = slogan

    def getNom(self):
        return self.__nom

    def setNom(self, newNom):
        if newNom.isalnum():
            self.__nom = newNom
            return True
        else:
            return False


    def __str__(self):
        return 'Ecole {}'.format(self.__nom)



class Personne:

    def __init__(self,nom, prenom, age=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Etudiant(Personne):
    
    def __init__(self,nom,prenom,age=0,matricule="00000"):
        Personne.__init__(self, nom, prenom)
        self.matricule = matricule

    def __str__(self):
        return f'{self.nom} {self.prenom} - Matricule : {self.matricule}'

p1=Personne('Diop','Amadou')

e1 = Etudiant('Ndiaye','Boubacar', matricule='BGHY00023')

print(p1)

print(e1)


'''
ecole1 = Ecole("ISI", adresse="Fass Pilote")


Ecole.getEmplacement()


print(ecole1.getNom())

nomprime=input("Merci d'indiquer le nouveau nom? ")

if ecole1.setNom(nomprime):
    print('Le nom de l\'établissement a été changé')
else:
    print('Des erreurs sont survenues. Merci d\'indiquer un nom alpha numérique')
'''