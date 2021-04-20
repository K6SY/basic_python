'''
    (*) Les if ...elif...else sont des instructions de type block
    (*) Les conditions évaluées doivent être des booléens
    (*) On peut avoir plusieurs elif
    

    Syntaxe:

    if condition:
        instuction1
        instruction2
    elif codition1:
        instuction3
        instruction4
    else:
        instuction5
        instruction6
'''

#Illustration: Equation du second degré
a=input('Merci d\'indiquer le monome de dégré 2\t')
b=input('Merci d\'indiquer le monome de dégré 1\t')
c=input('Merci d\'indiquer le monome de dégré 0\t')

a=int(a)
b=int(b)
c=int(c)
delta = (b**2) - (4*a*c)

if delta < 0:
    print("Pas de solutions dans IR")
elif delta == 0:
    x0=-b/(2*a)
    print(f"L'équation admet une solution unique X0={x0}")
else:
    x1=-b-delta**(1/2)/(2*a)
    x2=-b+delta**(1/2)/(2*a)

    #La fonction round permet d'arrondir
    x1_arrondi=round(x1,2)
    x2_arrondi=round(x2,2)
    print(f"L'équation admet deux solutions X1={x1_arrondi} et x2={x2_arrondi}")
