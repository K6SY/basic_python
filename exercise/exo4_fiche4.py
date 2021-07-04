L1= [17, 22, 5, 5, 33, 8] 
M1 = [34, 8, 20]

L2=[6, 22, 5, 5, 33, 8] 
M2 = [35, 8, 25]

def checkSomme42(L,M):
    somme42=False
    for i in L:
        for j in M:
            if i + j == 42:
                somme42=True
                break
    return somme42

print(checkSomme42(L1,M1))
print(checkSomme42(L2,M2))