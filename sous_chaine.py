'''
    Syntaxe sous-chaine: chaine[start:stop:step]

    (*) la valeur stop est exclu = L'extraction va s'arrêter à stop-1
    (*) Step est facultatif. Sa valeur par défaut est 1
    (*) Si l'extraction va jusqu'à la fin de la chaine alors, 
    la valeur stop peut être omise
    (*) Si l'extraction commence au début de la chaine alors, 
    la valeur start peut être omise


'''

chaine="Bonjour. Nous vous souhaitons la bienvenue"

#Extraction d'une sous-chaine allant de 0 à 6 par pas de 1
extrait1=chaine[0:7:1]
#Bonjour

#Extraction d'une sous-chaine allant de 0 à 6 par pas de 2
extrait2=chaine[0:7:2]

#Syntaxe Extraction en commançant par 0
extrait3=extrait1[:3]

#Syntaxe Extraction en terminant par la fin
extrait4=extrait1[3:]

#Algorithme reverse chaine dans le pire des cas

chaine2="Bonjour"

chaine2_reversed=""
n  = len(chaine2)

for i in range(n-1,-1,-1):
    #chaine2_reversed=chaine2_reversed+chaine2[i]
    chaine2_reversed+=chaine2[i]

print(chaine2_reversed)

#Algorithme d'inversion d'une chaine dans le meilleur des cas
chaine3_reversed = chaine2[::-1]
print(chaine3_reversed)

#print(extrait3)

#print(extrait4)