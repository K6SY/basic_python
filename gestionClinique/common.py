from patient import Patient
from medecin import Medecin
import db

def getMenu():
    print('''
        Bienvenue dans AppClinique
        --------------------------

        Selectionner le menu:

        - Taper 1 pour la gestion des patients

        - Taper 2 pour la gestion des medecins

        - Taper tout autre touche pour quitter
    ''')

def getSubMenu(menu):
    print(f'''
            ----------------------------------
            ##  Menu de Gestion des {menu}s ##
            ----------------------------------
            - Taper 1 pour ajouter un {menu}

            - Taper 2 pour lister les {menu}s

            - Taper 3 pour afficher les détails d'un {menu}

        ''')

def createPatient():
    nom = input('Entre le nom: ')
    prenom = input('Entre le prenom: ')
    sexe = input('Choisissez F ou M: ')
    telephone = input('Votre numéro de téléphone: ')
    return telephone, Patient(nom,prenom,telephone,sexe)

def createAndSavePatient():
    #Collecte données
    nom = input('Entre le nom: ')
    prenom = input('Entre le prenom: ')
    sexe = input('Choisissez F ou M: ')
    telephone = input('Votre numéro de téléphone: ')
    #Création d'un objet patient
    p1 = Patient(nom,prenom,telephone,sexe)

    #récupération des données sous forme de dictionnaire
    data = p1.__dict__

    #Sauvegarde dans la base
    cnx = db.dbConnect(db.config)
    db.insertPatient(cnx,data)
    db.dbDisconnect(cnx)


def getPatients():
    cnx = db.dbConnect(db.config)
    data = db.getAllPatient(cnx)
    db.dbDisconnect(cnx)
    return data

def getMedecins():
    cnx = db.dbConnect(db.config)
    data = db.getAllMedecin(cnx)
    db.dbDisconnect(cnx)
    return data


def createMedecin():
    nom = input('Entre le nom: ')
    prenom = input('Entre le prenom: ')
    sexe = input('Choisissez F ou M: ')
    matricule = input('Votre numéro de matricule: ')
    return matricule, Medecin(nom,prenom,matricule,sexe)

def createAndSaveMedecin():
    #Collecte données
    nom = input('Entre le nom: ')
    prenom = input('Entre le prenom: ')
    sexe = input('Choisissez F ou M: ')
    matricule = input('Votre numéro de matricule: ')
    specialite = input('Indiquer la specialite: ')
    #Création d'un objet patient
    m1 = Medecin(nom,prenom,matricule,sexe,specialite)

    #récupération des données sous forme de dictionnaire
    data = m1.__dict__

    #Sauvegarde dans la base
    cnx = db.dbConnect(db.config)
    db.insertMedecin(cnx,data)
    db.dbDisconnect(cnx)



def formatListePatient(data):
    print('-'*25)
    for item in data.values():
        print(f'| {item.nom} ',end="")
        print(f'| {item.prenom} ',end="")
        print(f'| {item.sexe} ',end="")
        print(f'| {item.telephone} ')
        print('-'*25)
    
def formatListeMedecin(data):
    print('-'*25)
    for item in data.values():
        print(f'| {item.nom} ',end="")
        print(f'| {item.prenom} ',end="")
        print(f'| {item.sexe} ',end="")
        print(f'| {item.matricule} ')
        print('-'*25)

def formatListePatientDB(data):
    print('-'*35)
    for item in data:
        print(f"| {item[0]} ",end="")
        print(f"| {item[1]} ",end="")
        print(f"| {item[2]} ",end="")
        print(f"| {item[3]} ")
        print('-'*35)

def formatListeMedecinDB(data):
    print('-'*35)
    for item in data:
        print(f"| {item[0]} ",end="")
        print(f"| {item[1]} ",end="")
        print(f"| {item[2]} ",end="")
        print(f"| {item[3]} ",end="")
        print(f"| {item[4]} ")
        print('-'*35)
