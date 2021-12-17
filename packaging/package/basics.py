def factorec(n):
    if n <= 1:
        return 1
    else:
        return n * factorec(n-1)

pi = 3.14

def palindrome(mot):
    mot_inverse=mot[::-1]
    print(mot_inverse)
    return mot == mot_inverse

#Fonction controle de saisie entier
def saisieEntier(message):
    a=input(message)
    while not a.isdigit():
        print("Merci de saisir un entier")
        a=input(message)
    return int(a)

#Fonction controle de saisie entier
def saisieGeneric(nature,message):
    a=input(message)
    if nature == 'ENTIER':
        while not a.isdigit():
            print("Merci de saisir un entier")
            a=input(message)
        a = int(a)
    elif nature == "CHAINE":
        pass
    return a

def creer_matrice():
    n=int(input("Indiquer la taille de la matrice: "))
    matrice=[]
    #construction des lignes
    for ligne in range(n):
        L=[]
        #Construction des colonnes
        for colonne in range(n):
            L.append(int(input(f"Entrer l'élément a{ligne+1}{colonne+1} : ")))
        matrice.append(L)
    return matrice

def afficherMatrice(M):
    n = len(M)
    for ligne in range(n):
        for colonne in range(n):
            print(M[ligne][colonne], end="\t")
        print()

def rotationQuartHorloge(M):
    n = len(M)
    for colonne in range(n):
        for ligne in range(n-1,-1,-1):
            print(M[ligne][colonne], end="\t")
        print()

def rotationQuartContraireHorloge(M):
    n = len(M)
    for colonne in range(n-1,-1,-1):
        for ligne in range(n):
            print(M[ligne][colonne], end="\t")
        print()

def showMessage(message):
    print()
    print("="*(10+len(message)))
    print(f"===> {message} <===")
    print("="*(10+len(message)))
    print()


def formatageTitre(chaine):
    l_contenu = len(chaine)+2
    bordure = "*"+"="*l_contenu+"*"
    contenu = "| "+chaine+" |"
    print(bordure,contenu,bordure,sep='\n')