'''
    (*)Les variables sont faiblement typés et nommés. 
        NB: Le type est implicite en Python

    (*) Quelques type de variable:
        - Simple
            * Entier (int)
            * Chaine de caracteres (str)
            * Boolean (bool) : True/False
            * Flottants (float)
        - Complexe
            * tuple
            * set
            * dictionnaire
            * liste
    (*) Nous utilisons le symbole (=) pour affecter une valeur à la variable.

    (*) La fonction input permet de récupérer la saisie au clavier
    (*) Le type de la variable récupérant la saisie de l'utilisateur est toujours <str>
'''

#Affection de variables
a = 5
b = 6.5
c = "Bonjour"
d = True

#Afficher le type des variables
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#Usage de la fonction input
nom = input('Donner votre nom ? \t')
prenom = input('Donner votre prenom ? \t')
age = input('Donner votre age ? \t')

'''
Formatage : Mixer dans l'affichage des variables et des chaines de caractères
'''
#Technique1
print('Bonjour Mr/Mme',prenom,nom,'.Vous avez',age,'ans')

#Technique 2
print('Bonjour Mr/Mme %s %s .Vous avez %s ans'%(nom,prenom,age))

#Technique 3
print('Bonjour Mr/Mme {} {} .Vous avez {} ans'.format(nom,prenom,age))

#Technique 4
print(f'Bonjour Mr/Mme {nom} {prenom} .Vous avez {age} ans')


#Affichage multiligne

print("Each observable variable can be enriched with a number of observers. \
An observer is a function (a kind of callback) which will be invoked automatically each time a specified event occurs in the variable’s life. \
The number of observers is not limited. \
Adding an observer to a variable is done by a method named trace(): obsid = variable.trace(trace_mode, observer)")