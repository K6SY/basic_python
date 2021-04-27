price=int(input("Merci de saisir le montant à payer\t"))

#Modulo est ue opératio permettant d'avoir le reste de la division entière
reste = price%20

if reste == 0:
    nbre_billet=price//20
else:
    nbre_billet=(price//20)+1

exc = (nbre_billet*20) - price

print(f"Pour payez un montant de {price}£, il vous faudra {nbre_billet} de 20£ et votre monnaie sera de {exc}£ ")