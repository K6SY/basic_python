L1=[]

n=int(input("Indiquer le nombre d'élément à ajouter sur la liste: "))

for i in range(n):
    L1.append(input(f'Indiquer la valeur {i+1}: '))

print(L1)

longueur = len(L1) # On pouvait utiliser directement n

if not(longueur%2 == 0):
    longueur=longueur-1

i=0

while i<longueur:
    L1[i],L1[i+1]=L1[i+1],L1[i]
    i+=2

print(L1)