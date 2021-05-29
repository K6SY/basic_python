
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


#Addition


chaine=saisieGeneric("CHAINE","Message de bienvenue: ")

print(type(chaine), ' --> ',chaine)

a=saisieGeneric("ENTIER","Donner le premier élément: ")

b=saisieGeneric("ENTIER","Donner le second élément: ")

c = a + b
print(f'{a} + {b} = {c}')