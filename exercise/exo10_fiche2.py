L=[1,3,5,7,8,10,12]

x = int(input('indiquer un numéro de mois entre 1 et 12: '))

message=f"Le mois N°{x} est un mois de 31 jours"

est_mois_31= x in L

if not est_mois_31:
    message = message.replace('est','n\'est pas')

print(message)