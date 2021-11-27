L = [31, 12, 9, 65, 81]

print("Avant permutation",L)
n = len(L)

if n%2 != 0:
    n -=1
    
for i in range(0,n,2):
    L[i],L[i+1] = L[i+1],L[i]

print("Après permutation",L)