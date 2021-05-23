'''
    (*) La fonction print permet d'afficher quelque chose à l'écran
    (*) Les commentaires permettent de documenter le code source: 
        * commentaire uniligne : on met # devant la ligne
        * commentaire multiligne: on met 3 quotes simples pour 
        indiquer la ligne de début et 3 quotes simples pour marquer la fin 
        NB: Les commentaires sont ignorés à l'execution
    (*) Les chaines de caratères sont délimités soit par 
    des quotes simples soit par des quotes doubles.
'''


#Afficher une chaine de caractère en python
print("Bonjour, Bienvenue dans mon blog")

#Afficher plusieurs chaines de caractères
print('Ceci est ma première chaine', "Ceci est ma deuxième chaine")

#Echappement d'un caractère avec le symbole \(antislash)
print('C\'est mon premier programme en python')
print("Ceci n'est pas un \"jeu\"")

#Modifier le comportement de print(afficher et retourner à la ligne)
print("Bonjour, Bienvenue dans mon blog", end=' $**$ ')

#Le séparateur dans print
print('Ceci est ma première chaine', "Ceci est ma deuxième chaine",sep=' *** ')

