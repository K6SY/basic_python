'''
    Les opérateurs classiques que nous avons:

    +  : addition
    -  : soustraction
    *  : Multiplication
    /  : Division réelle
    // : Division entière
    %  : Module (reste de la division)
    ** : Puissance

    NB: Input renvoie uniquement des strings. Pour utiliser la 
    valeur saisie avec un autre type, il faudra la caster
'''

#Equation du second degré dans IR : ax2 + bx +c =0

a=input('Merci d\'indiquer le monome de dégré 2\t')
b=input('Merci d\'indiquer le monome de dégré 1\t')
c=input('Merci d\'indiquer le monome de dégré 0\t')

#Casting des variables : Changement de type
a=int(a)
b=int(b)
c=int(c)
delta = (b**2) - (4*a*c)
print(delta)

'''
A continuer dans le fichier contole.py pour les solutions
'''