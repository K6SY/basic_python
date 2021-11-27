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


m = creer_matrice()
showMessage("Matrice normale")
afficherMatrice(m)
showMessage("Transposée Matrice sens aiguille montre")
rotationQuartHorloge(m)
showMessage("Transposée Matrice sens contraire aiguille montre")
rotationQuartContraireHorloge(m)
