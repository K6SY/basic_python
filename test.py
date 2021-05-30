x=int(input("Merci de rentrer un entier? \n"))
y=int(input("Merci de rentrer un entier? \n"))

print()
print("#### Normal way ######")
for i in range(1,y+1):
    print(f"{x} x {i} = {x*i}")

print("#### Reverse way ######")
for i in range(y,0,-1):
    print(f"{x} x {i} = {x*i}")

print("#### Odd numbers : Reverse way ######")
if y%2 != 0:
    y-=1
for i in range(y,0,-2):
    print(f"{x} x {i} = {x*i}")