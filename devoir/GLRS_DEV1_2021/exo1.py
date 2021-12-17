def est_croissante(L):
    n = len(L)
    retour = True
    for i in range (n-1):
        if L[i]>L[i+1]:
            retour = False
            break
    return retour

def est_croissante_while(L):
    n = len(L)
    i=0
    while (i<n-1 and L[i]<=L[i+1]):
        i+=1
    return i == n-1



L=[5, 6, 6, 6, 10]
L1=[5, 6, 6, 6, 4, 5 ] 

print(est_croissante(L1))
print(est_croissante_while(L1))

