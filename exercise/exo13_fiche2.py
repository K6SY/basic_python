L = [31, 12, 9, 65,10]

'''
L1=L[::-1]


L.reverse()
print("Après inversion",L)
print("Après inversion",L1)
'''

print("Avant inversion",L)
n=len(L)

m=n//2

for i in range(m):
    L[i],L[n-i-1]=L[n-i-1],L[i]

print("Après inversion",L)
