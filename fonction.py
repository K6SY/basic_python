'''
En Math
- Représentation d'un résultat dans un domaine de définition
La fonction est définie par:
    IR   ---->  IR
    x    |--->   f(x)=2x+1

L'appel à la fonction:
x=1, f(1)=3
x=5, f(5)=11
etc...

En Python

    - Factoriser le code pour centraliser les modifications
    - Favoriser l'ergonomie et la maintenabilité

    Ex: print() et input() sont des fonctions built-ins

    - Le mot clé << def >> permet de créer une focntion

    - Une fonction prend 0 ou plusieurs paramètres

    - Une fonction retourne toujours une valeur.

    - Il existe 2 types de paramètres
        * Les paramètres positionnels
        * Les paramètres nommés
    NB: 
        (*) Les paramètres nommés vient toujours après les paramètres positionnels
        (*) Les paramètres nommés permettent de définir des valeurs par défaut
        (*) Les paramètres positionnels indiqués à la définition sont nominatifs
    NB: Une fonction qui ne retourne pas de valeur est appelée une procédure

    - La syntaxe de la definition:

        def nomFonction(param1, param2,...,paramN):
            Instructrion1
            Instruction2

            return valeur
        print()
    - La syntaxe de l'appel
        nomVariable = nomFonction(param1, param2,...,paramN)


#Exemple 1: Le factoriel avec parametre

def factoriel(n):
    if n <= 1:
        return 1
    else:
        valeur=1
        for i in range(1,n+1):
            valeur=valeur*i
        return valeur


z=int(input("Indiquer un nombre\t"))
resultat=factoriel(z)

print(f"Le factoriel de {z} est de {resultat}")

'''

#Exemple 2: Le factoriel sans paramètre

def facto():
    n=int(input("Indiquer un nombre\t"))
    if n <= 1:
        return n,1
    else:
        valeur=1
        for i in range(1,n+1):
            valeur=valeur*i
        return n,valeur

z,resultat=facto()

print(f"Le factoriel {z} est de {resultat}")

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


r = loterie(1,100)
r1 = loterie(1,100,nbre=10)

print(r)
print(r1)

#Fonction récursive

def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n * factoriel(n-1)