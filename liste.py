'''
    (*) Définition d'une liste: 
        variable = [valeur1, valeur2, ...,valeurN ]
    (*) Le indices sont nuémriques, continues et auto-incrémentés
    (*) Les valeurs peuvent être de tout type (simple comme complexe)
    (*) Les listes sont modifiables
    (*) Les indices commencent par 0
    (*) De la gauche vers la droite les indices sont positifs
    (*) De la droite vers la gauche les indices sont négatifs
'''

#Création d'une liste vide

l1=[]
l2=list()

#Création d'ue liste avec des valeurs
t1=(1,'Juin',2021)
l3=['Bonjour','DIT4',12,2021,135.76,t1]

#Accèder à un élément de la liste
print(l3[4])


#Ajouter un élément dans une liste (les éléments sont toujours ajoutés à la fin )
#print(l1)
l1.append('Bonsoir')
#print(l1)
l1.append(2021)
#print(l1)
#l1.clear()
#print(l1)

#Utilisation de la fonctio copy pour créer une copie indépendante

l3_prime=l3.copy()
l3_prime.append(12)
#print(l3)
#print(l3_prime)

#Count renvoie le nombre  d'occurence d'une value
n=l3_prime.count(12)
#print(n)


#La fonction extend permet d'étendre une liste
#print(l1)
#print(l3)

l3.extend(l1)
#print("####")

#print(l1)
#print(l3)

#Insert permet d'ajouter une valeur à une position spécifique

print(l1)
l1.insert(1,'Intrus')
print(l1)

print("####")

#Pop permet de supprimer un élément à partir de son indice et renvoie la valeur supprimer
valeur=l1.pop(1)
#print(valeur)
#print(l1)

#Remove permet de supprimer une valeur de la liste

l1.remove("Bonsoir")
#print(l1)


#Reverse permet d'inverser une liste
#Sort permet de trier par ordre

l1 = [1,6,14,3,67,90,23]
l1.reverse()
l1.sort(reverse=True)
#print(l1)

#Sous-liste

l1 = [1,6,14,3,67,90,23]
l2 = l1[0:3:1]

n = len(l2)
#parcourir une liste : technique 1
for i in range (n):
    print(f'{l2[i]} est à l\'indice {i}')

print('########')

#parcourir une liste : technique 2
for i in l2:
    #La fonction index permet d'avoir l'indice d'un élément dans un tuple
    print(f'{i}')

