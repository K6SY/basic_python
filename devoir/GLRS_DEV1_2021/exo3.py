def divisi (n):
    nbre_division=0
    while n>1:
        if n%2 != 0:
            n+=1
        n = n//2
        print(n,end=" ")
        nbre_division+=1
    print()
    return nbre_division

print('Nombre de division: ',divisi(42))
