#Installation du connecteur MySQL pour python
#python3 -m pip install mysql-connector-python
from mysql.connector import connect, Error, errorcode

config = {
  'user': 'root',
  'password': 'Soroc2022',
  'host': '127.0.0.1',
  'database': 'gestionclinique',
  'raise_on_warnings': True
}


#Fonction permet d'établir une connexion à votre base de donnée
def dbConnect(yourconfig):
  cnx=''
  try:
    cnx = connect(**yourconfig)
  except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print ("Database does not exist")
    else:
      print("Some errors are occured")
  return cnx

#Fonction permet de mettre à une connexion à votre base de donnée
def dbDisconnect(cnx):
    cnx.close()

def insertPatient(cnx,data):
    sql = f"INSERT INTO patient (nom,prenom,sexe,telephone) VALUES (%s,%s,%s,%s)"
    data_list = [data['nom'],data['prenom'],data['sexe'],data['telephone']]
    cursor = cnx.cursor()
    cursor.execute(sql,data_list)
    cnx.commit()
    return True

def getAllPatient(cnx):
    sql="Select * from patient"
    cursor = cnx.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def insertMedecin(cnx,data):
    sql = f"INSERT INTO medecin (nom,prenom,sexe,matricule,specialite) VALUES (%s,%s,%s,%s,%s)"
    data_list = [data['nom'],data['prenom'],data['sexe'],data['matricule'],data['specialite']]
    cursor = cnx.cursor()
    cursor.execute(sql,data_list)
    cnx.commit()
    return True

def getAllMedecin(cnx):
    sql="Select * from medecin"
    cursor = cnx.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
