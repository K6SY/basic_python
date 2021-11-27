def repeter(L):
    L2 = L.copy()
    L2.extend(L)
    return L2

def repeter_v1(L):
    L2=[]
    for j in range(2):
        for i in L:
            L2.append(i)
    return L2

def repeter_v2(L):
    return L+L

L=[1000, 81, 12]

print(repeter(L))
print(repeter_v1(L))
print(repeter_v2(L))