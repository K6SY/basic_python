def mini(L, debut):
    minimum = L[debut]
    for i in range (debut+1,len(L)):
        if L[i]%2 ==0 and L[i]<minimum:
            minimum = L[i]
    return minimum

def ind_elt_pair(L):
    pluspetitpair=-1
    for i in range (len(L)):
        if L[i]%2 == 0:
            pluspetitpair=i
            break
    return pluspetitpair


def miniPairs(L):
    debut = ind_elt_pair(L)
    pluspetit = mini(L, debut)
    return pluspetit
    #return mini(L,ind_elt_pair(L))

L=[81, 32, 10, 21, 42, 11, 12, 9, 12, 65, 46]
debut=4

L=[81, 32, 12, 9, 12, 65, 46]

print(miniPairs(L))