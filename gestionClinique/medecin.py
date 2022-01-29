from personne import Personne
class Medecin(Personne):

    def __init__(self,nom, prenom,matricule,sexe="M",specialite="Generaliste"):
        super().__init__(nom, prenom,sexe)
        self.matricule = matricule
        self.specialite = specialite

    def __str__(self):
        return f"{self.prenom} {self.nom} (matricule : {self.matricule}) "