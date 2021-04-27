#Collecte des données

j=int(input("Merci d'indiquer le jour?\t"))
m=int(input("Merci d'indiquer le mois?\t"))


#if (j>0 and j<32) and (m>0 and m<13):
if (1<=j<=31 and 1<=m<=12):

    #Solution de l'exercice
    enVacances=(8<=j<=31 and m==7)or(1<=j<=31 and m==8)or(1<=j<=3 and m==9)
    
    if enVacances:
        print(f"Pour la date du {j}-{m}-2021, vous serez en vacances")
    else:
        print(f"Pour la date du {j}-{m}-2021, vous ne serez pas en vacances")
else:
    print("Désolé. Vous n'avez pas saisi une date valide")