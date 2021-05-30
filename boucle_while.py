'''
    Les boucles sont des instructions de types block

    while conditions:
        instructions
        instruction_speciale

'''
#Pratique: Table de multiplication de x par y saisi au clavier

x=int(input("Merci de rentrer un entier? \n"))
y=int(input("Merci de rentrer un entier? \n"))

print()
print("#### Normal way ######")
i=1
while i<=y:
    print(f"{x} x {i} = {x*i}")
    i+=1

print()
print("#### Reverse way ######")
i=y
while i>0:
    print(f"{x} x {i} = {x*i}")
    i-=1

'''
    abrégé quelques opérations arithmetiques

    i=i+1    ----> i+=1
    i=i-1    ----> i-=1
    i=i*1    ----> i*=1
    i=i/1    ----> i/=1
    i=i//1    ----> i//=1

'''

#L'instruction break : Permet de sortir complétement de la boucle
#Descendant
print("#### Reverse way with break ######")
cpt=y
while True:
    if cpt >= 1:
        z = x * cpt
        print(f"{x} x {cpt} = {z}")
        cpt=cpt-1
    else:
        break

#L'instruction continue : Permet d'ignorer le reste des instructions d'une itération et passe à l'itération suivante
print("#### Odd numbers : Reverse way with continue ######")
cpt=y
while cpt >= 1:
    if cpt%2 != 0:
        cpt=cpt-1
        continue
    z = x * cpt
    print(f"{x} x {cpt} = {z}")
    cpt=cpt-1