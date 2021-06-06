'''
    Les boucles sont des instructions de types block

    NB: 
        (*) Si le paramètre step est omis, alors le pas par défuat est de 1

        (*) La valeur stop est exclusif (la boucle s'arrêtera à stop-1)


    Syntaxe

    for compteur in range(start=0, stop=n, step=1):
        instrunction

    for compteur in range(start=0, stop=n):
        instrunction

    for compteur in range(stop=n):
        instrunction

'''

#Pratique: Table de multiplication de x par y saisi au clavier

x=int(input("Merci de rentrer un entier? \n"))
y=int(input("Merci de rentrer un entier? \n"))

print()
print("#### Normal way ######")
for i in range(1,y+1):
    print(f"{x} x {i} = {x*i}")

print()
print("#### Reverse Way ######")
for i in range(y,0,-1):
    print(f"{x} x {i} = {x*i}")


'''
    Parcours d'un objet:
    
    for compteur in object:
        instructio

'''

print()
print("#### Boucle for parcours chaine ######")

chaine='DIT4 2021'

for i in chaine:
    print(i,end='*')
print()