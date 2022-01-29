'''
Cette classe reprèsente une personne
'''

class Personne():
    def __init__(self,nom,prenom,sexe="M"):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
    
    def __repr__(self):
        return f"<Personne> : {self.prenom} {self.nom}"
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"