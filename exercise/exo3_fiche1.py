'''
x=2 + 3 * 5
y=(2 + 3) * 5
z=2 + (3 * 5)
print (x==y, x==z)
'''

#La puissance est prioritaire à la soustraction
a = -1 ** 2
b = -(1**2)
c = (-1)**2

#Si on a que des puissances dans l'expression, la priorité c'est de la droite vers la gauche
a = 10 ** 2 ** 3
b = (10 ** 2) ** 3
c = 10 ** (2 ** 3)

print (a==b, a==c)