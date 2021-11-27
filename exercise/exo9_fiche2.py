a=2
b = -3
c=1
L=[]
delta = b*b -4*a*c 
if delta >0:
    print("2 solutions distinctes :")
    x1 = (-b - delta**0.5)/(2.*a)
    x2 = (-b + delta**0.5)/(2.*a)
    print("x1 =", x1)
    print("x2 =", x2)
    L.append(x1)
    L.append(x2)
else:
    if delta == 0:
        print("une seule solution")
        x0=(-b)/(2.*a)
        print("x =", x0) 
        L.append(x0)
    else:
        print("Aucune solution")

print(L)