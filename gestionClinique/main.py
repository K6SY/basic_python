
from common import *
import db

#nom = input('Entre le nom: ')
#prenom = input('Entre le prenom: ')
#sexe = input('Choisissez F ou M: ')
#matricule = input('Entre votre matricule: ')

#p1 = Medecin(nom,prenom,matricule,sexe)
annuairePatient={}
annuaireMedecin=dict()

while True:
    getMenu()
    choix = int(input('Merci d\'indiquer votre choix'))
    print()
    if choix == 1:
        getSubMenu('patient')
        action = int(input('Merci d\'indiquer l\'action à faire'))
        if action == 1:
            #Usage Dictionnaire
            #key,p = createPatient()
            #annuairePatient[key]=p

            #Usage Base de donnée
            createAndSavePatient()
            print('Patient ajouté avec succès')
        elif action == 2:
            #Usage Dictionnaire
            formatListePatient(annuairePatient)

            #Usage Database
            data = getPatients()
            formatListePatientDB(data)
        elif action == 3:
            pass
        else:
            print("Choix Incorrect")
    elif choix == 2:
        getSubMenu('medecin')
        action = int(input('Merci d\'indiquer l\'action à faire'))
        if action == 1:
            #Usage Dictionnaire
            #key,p = createMedecin()
            #annuaireMedecin[key]=p

            #Usage Base de donnée
            createAndSaveMedecin()
            print('Medecin ajouté avec succès')
        elif action == 2:
            #Usage Dictionnaire
            #formatListeMedecin(annuaireMedecin)
            
            #Usage Database
            data = getMedecins()
            formatListeMedecinDB(data)

        elif action == 3:
            pass
        else:
            print("Choix Incorrect")
    else:
        break
    print()
