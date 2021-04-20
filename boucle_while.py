'''
    Les boucles sont des instructions de types block

    while condition:
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
