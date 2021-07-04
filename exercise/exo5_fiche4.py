L = [81, 31, 81, 12, 81, 9, 12, 65]

M=list()
for i in L:
    if i not in M:
        apparition = L.count(i)
        M.append(i)
        print(f'{i} : {apparition}')