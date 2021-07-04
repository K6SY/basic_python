class Vehicule:
    quantite=0
    #Constructeur de la classe
    def __init__(self, marque="Generic", moteur="Essence",cartegrise=None):
        self.marque = marque
        self.moteur = moteur
        self.__cartegrise=cartegrise
    
    def setCG(self, cartegrise):
        self.__cartegrise=cartegrise
    
    def getCG(self):
        return self.__cartegrise


    def whois(self):
        print(f"Je suis un véhicule de Marque {self.marque} et de moteur {self.moteur}")