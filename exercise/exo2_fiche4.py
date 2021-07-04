'''
    Addition de 2 nombre pairs --> nombre pair
    Addition de 2 nombre impairs --> nombre pair
    Addition d'un nombre pair et d'un nombre impair --> nombre impair
'''
print("Question1")
print("----------------")
a = int(input('Donner une valeur pour a \n'))
b = int(input('Donner une valeur pour b \n'))
#Question1: Même parité
memeParite = (a+b)%2 == 0
#memeParite = ((a%2 == 0) and (b%2 == 0)) or ((a%2 != 0) and (b%2 != 0))
print(f'{a} et {b} ont même parité : {memeParite}')
print()
#Question2: Affichage Damier
print("Question 2")
print("----------------")
n = 5
nombre = 4
L=[]
for i in range (n):
    L1=[]
    for j in range (n):
        L1.append(nombre)
        if nombre == 4:
            nombre -=2
        else:
            nombre +=2
    L.append(L1)

print(L)

for i in L:
    for j in i:
        print(j, end=' ')
    print()