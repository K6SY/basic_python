'''
    (*) Définition d'un tuple: 
        variable = (valeur1, valeur2, ...,valeurN )
    (*) Le indices sont nuémriques, continues et auto-incrémentés
    (*) Les valeurs peuvent être de tout type (simple comme complexe)
    (*) Les tuples ne sont pas modifiables
    (*) Les indices commencent par 0
    (*) De la gauche vers la droite les indices sont positifs
    (*) De la droite vers la gauche les indices sont négatifs
'''

t1=(1, 2.5, 'Bonjour', True)

t2=('ISI', t1, False)

print(t1)

#Accéder au élément d'un tuple
#print(t1[-1])
#print(t1[1])

#Les sous-tuples (A l'image des sous-chaine)
t_prime=t1[0:3]
#print(t_prime)


#Inversion tuple
it1 = t1[::-1]

#Avoir la longueur d'un tuple

n=len(t2)

#parcourir un tuple : technique 1
for i in range (n):
    print(f'{t2[i]} est à l\'indice {i}')

print('########')

#parcourir un tuple : technique 2
for i in t2:
    #La fonction index permet d'avoir l'indice d'un élément dans un tuple
    indice = t2.index(i)
    print(f'{i} est à l\'indice {indice}')

print('#####*****###')

#Accès à un tuple de tuple

print(t2[1][2])
print(t2[-1][l1-1])
print(t2[-1][-1])


#permutation de valeur avec les tuples

a = 10
b = 25

print(a,b)

(a,b) = (b,a)

print(a,b)

#Affectation multiple grâce au tuple
a,b,c,d,e = 12,15.2,False,"Chaine",(1,2,3,4)



#Concaténation de tuples
semestre1=("Janvier","Fevrier", "Mars", "Avril","Mai","Juin")
semestre2=("Juillet","Aout","Septembre","Octobre","Novembre","Decembre")

an = semestre1 + semestre2

#Utilisation des tuples domme valeurs de retour d'ue fonction

def factoriel():
    n = int(input('Veuillez indiquer un nombre'))
    fact=1
    for i in range(2,n+1):
        fact*=i
    return (n,fact)

nombre,resultat=factoriel()
print(f"Le factoriel de {nombre} est de {resultat}")
