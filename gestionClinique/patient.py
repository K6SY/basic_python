from personne import Personne
class Patient(Personne):

    def __init__(self,nom, prenom,telephone,sexe="M"):
        super().__init__(nom, prenom,sexe)
        self.telephone = telephone

    def __str__(self):
        return f"{self.prenom} {self.nom}( Telephone :{self.telephone})"