n=int(input('Donner un entier n positif :  '))
res=0
for i in range(1,n+1):
    res=res+i # res+=i
print(res)

test = res == n*(n+1)/2

print(test)
