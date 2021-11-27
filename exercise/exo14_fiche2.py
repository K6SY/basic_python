x=int(input('Entrer x : '))
y=int(input('Entrer y : '))


ok = (1<=x<=4 and 1<=y<=4) and ((x==y+1 or y==x+1) or ((x==1 and y==4) or (x==4 and y==1)))

print(ok)