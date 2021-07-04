#Fonction avec paramètre positionnels et nommés
def loterie(start,stop,nbre=1):
    resultat=""
    if nbre != 1:
        for i in range(nbre):
            choix = randint(start,stop)
            resultat = resultat + str(choix) + " "
    else:
        resultat = str(randint(start,stop))
    
    return resultat

def createMatrice():
    n=int(input('Indiquer la taille de votre matrice: '))
    matrice=[]

    for i in range(n):
        L=[]
        for j in range(n):
            value = int(input(f'Donner la valeur a{i+1}{j+1}: '))
            L.append(value)
        matrice.append(L)
    
    return matrice

def rotateMatrice(matrice):
    n = len(matrice)
    new_matrice=[]
    for j in range(n):
        L=[]
        for i in range(n-1,-1,-1):
            L.append(matrice[i][j])
        new_matrice.append(L)
    return new_matrice

def antirotateMatrice(matrice):
    n = len(matrice)
    new_matrice=[]
    for j in range(n-1,-1,-1):
        L=[]
        for i in range(n):
            L.append(matrice[i][j])
        new_matrice.append(L)
    return new_matrice