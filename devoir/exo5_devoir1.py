def divisi(n):
    nbre_division=0
    while n>1:
        if n%2 == 0:
            n = n//2
        else:
            n = (n+1)//2
        print(n,end=' ')
        nbre_division=nbre_division+1
    print()
    return nbre_division

print("Le nombre de division",divisi(38))