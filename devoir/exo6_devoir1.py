def mini(L,debut):
    plus_petit_pair = L[debut]

    for i in range(debut+1,len(L)):
        if L[i]%2 == 0 and L[i]<plus_petit_pair:
            plus_petit_pair = L[i]
    
    return plus_petit_pair

def  ind_elt_pair(L):
    n = len(L)
    i=0
    while i<n:
        if L[i]%2 == 0:
            break
        i=i+1
    return i

def miniPairs(L):
    debut = ind_elt_pair(L)
    plus_petit_pair = mini(L,debut)
    return plus_petit_pair

    #return mini(L,ind_elt_pair(L))

L=[81, 65, 46]
print(miniPairs(L))


