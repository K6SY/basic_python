n = int(input("Veuiller entrer un entier n \t"))

#question 1
def niemeNombre(n):
    nombre=0
    for i in range(n):
        nombre += 10**i
    return nombre

#Question2
N=20
resultat=0
for i in range(N):
    resultat+=niemeNombre(i)
print(resultat)