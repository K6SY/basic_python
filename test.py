

'''
    Définition
        Tuple : ()
        Liste: []
        Dictionnaire: {}

    Accès:
        Tuple, Liste, Dictionnaire: []
    
'''

#Création de liste vide
l1 = list()
l2 = []

#Création d'une liste avec des valeurs
l3=[12,24.5,"Bonjour",True]

#Accèder à un élément de la liste
#print(l3[2])

#Ajout d'élémets avec append
#print(l1)
l1.append('ISI')
#print(l1)
l1.append(2021)
#print(l1)
l1.append("Seminaire")
#print(l1)

#Supprimer les éléments d'une liste
#l1.clear()
#print("Après un clear, l1 vaut : ",l1)

#Utilisation de la fonctio copy pour créer une copie indépendante

#print(l1)
l2 = l1.copy()
#print(l2)
l2.append(2021)
#print(l2)
#print(l1)

#Count renvoie le nombre  d'occurence d'une value
#print(l2)
#print(l2.count(2021))

#La fonction extend permet d'étendre une liste

#print(l3)
#print(l2)
l2.extend(l3)
#print(l2)

#Insert permet d'ajouter une valeur à une position spécifique

#print(l2)
l2.insert(1,'Intrus')
#print(l2)

#Pop permet de supprimer un élément à partir de son indice et renvoie la valeur supprimer
#print(l2)
valeur=l2.pop(1)
#print('Elements supprimés : ',valeur)
#print(l2)

#Remove permet de supprimer une valeur de la liste
l2.remove(2021)
#print("Suppressio 2021 : ",l2)

#Sous-liste

l1 = [1,6,14,3,67,90,23]
l2 = l1[0:3:1]

#Reverse permet d'inverser une liste
#Sort permet de trier par ordre

l1 = [1,6,14,3,67,90,23]
print("Normale", l1)
l1.reverse()
print("Inversé", l1)
l1 = l1[::-1]
print("Inversé Bis",l1)

l1.sort()
print("Liste - tri croissant",l1)

l1.sort(reverse=True)
print("Liste - tri décroissant",l1)