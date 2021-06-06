
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

def affichage(matrice):
    n=len(matrice)
    print("__"," "*13,"__")
    for i in range(n):
        print("| ", end="")
        for j in range(n):
            if j < n-1:
                print(matrice[i][j],end='\t')
            else:
                print(matrice[i][j],end='')
        print(" |",end="")
        print()
    print("__"," "*13,"__")


print("Matrice")
m1 = createMatrice()
affichage(m1)
print("Matrice : Rotation 1/4 dans le sens des aiguilles d'une montre")
m2=rotateMatrice(m1)
affichage(m2)

print("Matrice : Rotation 1/4 dans le sens contraire des aiguilles d'une montre")
m3=antirotateMatrice(m1)
affichage(m3)