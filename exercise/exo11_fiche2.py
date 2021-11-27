L = [31, 12, 9, 65, 81]

#Solution1

'''
print("Avant échange:",L)
tampon=L[0]
L[0]=L[-1]
L[-1]=tampon
print("Après échange:",L)
'''

#Solution2
print("Avant échange:",L)
L[0],L[-1]=L[-1],L[0]
print("Après échange:",L)