def repeter(L):
    return L*2

def repeter1(L):
    n = len(L)
    M=[]
    for i in range(2):
        for j in L:
            M.append(j)
    return M


def repeter2(L):
    return L+L

def repeter3(L):
    M = L.copy()
    M.extend(L)
    return M


L=[1000, 81, 12] 



print(repeter3(L))
#print(repeter1(L))