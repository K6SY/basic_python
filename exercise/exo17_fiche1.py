a=int(input("Donner la valeur de a"))
b=int(input("Donner la valeur de b"))
c=int(input("Donner la valeur de c"))
if (b<=a <=c or c<=a<=b):
    print(f"{a} est l'élément central")
if(a<=b<=c or c<=b<=a):
    print(f"{b} est l'élément central")
if (a <= c <= b or b <= c <= a):
    print(f"{c} est l'élément central")