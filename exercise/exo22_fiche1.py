n=int(input("Indiquer la valeur de n?\t"))
reste=n%5

#Question 1 
if reste <=2:
    N=n-reste
else:
    N= n + (5-reste)
print(f"Q1 - {N} est le multiple de 5 le plus proche de {n}")

#Questio2

m = round(n/5)*5
print(f"Q2 - {m} est le multiple de 5 le plus proche de {n}")

h=int(input("Merci d'indiquer l'heure?\t"))
m=int(input("Merci d'indiquer le nombre de minutes?\t"))

#if (j>0 and j<32) and (m>0 and m<13):
if (0<=h<=23 and 0<=m<=59):
    M=round(m/5)*5
    if M == 60:
        M = 0
        if h == 23:
            H = 0
        else:
            H = h+1
    else:
        H = h
else:
    print("Désolé. Vous n'avez pas saisi une heure valide")

print(f"{h}h {m}m -> [{H}, {M}]")