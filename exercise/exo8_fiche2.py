L=[31,12,42,9,65]
L1=[31,12,81,43]
L2=[41]
L3=[31,12,81,9,65]

x=42

ok= (x in L) or (x+1 in L) or (x-1 in L)
ok1= (x in L1) or (x+1 in L1) or (x-1 in L1)
ok2= (x in L2) or (x+1 in L2) or (x-1 in L2)
ok3= (x in L3) or (x+1 in L3) or (x-1 in L3)

print(L,ok,sep=' --> ')
print(L1,ok1,sep=' --> ')
print(L2,ok2,sep=' --> ')
print(L3,ok3,sep=' --> ')
