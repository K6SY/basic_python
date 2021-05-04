'''
    les chaines sont délimités par :
        - des quotes doubles ("contenu de la chaine")
        - des quotes simples ('contenu de la chaine')
'''

chaine1="J'ai cours de python tous les Mardis"
chaine2='En tant qu\'informaticien, je veux apprendre python'

'''
    - Longueur d'une chaine : Usage de la fonction len qui renvoie le 
    nombre de caractères de la chaine

    Syntaxe: variable = len(chaine)

    NB: les espaces, les caractères spéciaux sont comptabilisés

    - Fonctions spécifiques: Les fonctions qui ne peuvent être utilisés
    que par un type de données bien précis.

    Syntaxe Fonction specifique: variable.fonction()
    Syntaxe Fonction specifique: fonction(variable)

    - Obtenir de l'aide pour les chaines: 
        * Executer la commande python
        * help(str)

    - Les chaines de caractères sont indexés. 
    - Les index sont numériques, commencent par 0 et sont incrémentés et continus

    -----------------------------
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
    -----------------------------
    | B | O | N | J | O | U | R |
    -----------------------------
    | -7| -6| -5| -4| -3| -2| -1|
    -----------------------------
    - Pour accéder aux caractères d'une chaine, voici la syntaxe:
        chaine[index]
    
    - De la gauche vers la droite, les index sont positifs
    - De la droite vers la gauche, les index sont négatifs


    - Une sous-chaine est obtenue grâce à la syntaxe: 
        chaine[start:stop:step]

        (*) start indique l'index de départ
        (*) stop est une valeur exclusive et indique l'index d'arrivée (stop-1)
        (*) step c'est le pas
        (*) aucun des paramètres n'est obligatoire

'''
a=len(chaine1)
b=len(chaine2)
print('La longueur de la chaine 1  : {}'.format(a))
#print('La longueur de la chaine 2 : {}'.format(b))

#Captilize - Lower - Upper - isupper - islower
ch1 = "JE SUIS UNE CHAINE EN MAJUSCULE"
ch2 = ch1.capitalize()
ch3 = ch2.upper()
ch4 = ch3.lower()
#print(ch1.isupper())
#print(ch2.islower())
#print(ch4.islower())

#Accès aux cractères d'une chaine
ch1="BONJOUR"
last=len(ch1)-1
#print(ch1[last])
#print(ch1[-2])

#La fonction count : retourner le nombre d'occurence d'une sous-chaine
ch1="on ne veut pas de ce mouton car il n'est pas bon"

#print(ch1.count('e'))
#print(ch1.count('e',2))
#print(ch1.count('e',2,6))
#print(ch1.endswith('bo'))
#print(ch1.startswith('ne',3,6))



#Création d'une fonction pour la saisie d'un entier
#usage isalpha - isdigit
def entier():
    n = input("Merci de saisir un entier?\t")
    while True:
        if n.isdigit():
            n=int(n)
            break
        else:
            print("Désolé. Vous n'avez pas saisi un entier.")
            n = input("Merci de saisir un entier?\t")
    return n
    #print(n.isalpha())
    #print(n.isdigit())


#Usage du replace

chaine1=input("Merci de saisir votre resenti?\n")
#print('-------')
#print(chaine1)
chaine2=chaine1.replace('bien','mal')
#print(chaine2)

#Sous-chaine
ch1="on ne veut pas de ce mouton car il n'est pas bon"

#Sous-chaine  : Tous les paramètres
ssch1 = ch1[0:27:1]

#Sous-chaine : absence start
ssch1 = ch1[:27]

#Sous-chaine : absence stop,step
ssch2 = ch1[27:]

#Sous-chaine : absence start,stop
ssch3 = ch1[:]

#Inverser une chaine
ssch4 = ch1[::-1]

print(ssch1)
print(ssch2)
print(ssch3)
print(ssch4)

