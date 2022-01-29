from datetime import datetime

class Consultation():

    def __init__(self,patient,medecin,motif="Consultation simple"):
        self.dateConsultation = datetime.now()
        self.patient = patient
        self.medecin = medecin
        self.motif = motif

    def __str__(self):
        return f'Consultation en date du {self.dateConsultation} - Medecin : {self.medecin} - Patient:{self.patient} - Motif: {self.motif}'