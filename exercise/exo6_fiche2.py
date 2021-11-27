L=[31,12,81,9,65]

k = int(input('Entrer un indice:'))

if 0<k<=len(L):
    print(k,L[k-1],sep=" -> ")
else:
    print(k,"-> rang invalide")