def est_croissante(L):
    n = len(L)
    croissant=False
    for i in range (n-1):
        if L[i]<=L[i+1]:
            croissant = True
        else:
            croissant = False
            break
    return croissant

def est_croissante_v1(L):
    n = len(L)
    croissant=True
    for i in range (n-1):
        if L[i]>=L[i+1]:
            croissant = False
            break
    return croissant

L=[5, 6, 6, 6, 4, 5 ]

print(L,"-->",est_croissante(L))