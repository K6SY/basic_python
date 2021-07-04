

#Définition d'un dictionnaire vide

d1={}

d2=dict()

#Définition d'un dictionnaire avec initialisation de valeurs

d3={'nom': 'Fall', 'prenom':'Samba', 'classe':'DIT4'}

#Accès aux données

#print(f"L'étudiant(e) {d3['prenom']} {d3.get('nom')} est inscrit(e) en classe de {d3['classe']}")

#insertion de données
#print(d2)
#d2 contient les notes
d2['python']=12
d2['java']=16
d2['php']=18
#print(d2)

d1['etudtiant']=d3
d1['notes']=d2
#print(d1)

#Récupérer la liste des clés
#print("Les clés de D3:",d3.keys())

#Récupération des valeurs
#print("Les valeurs de D3:",d3.values())

#Récupéartions clé et valeurs
#print("Les clés, valeurs de D3:",d3.items())


#Parcourir un dictionnaire : Technique 1

print("Technique 1")
for i in d3.keys():
    print(f" La valeur \"{d3.get(i)}\" est associée à la clé \"{i}\"")

print()

#Parcourir un dictionnaire : Technique 2

print("Technique 2")
for i in d3.values():
    print(i,end=' *** ')

print()

#Parcourir un dictionnaire : Technique 1
print()
print("Technique 3")
for i,j in d3.items():
    print(f" La valeur \"{j}\" est associée à la clé \"{i}\"")

print()