#Importation du module randint
from random import randint


print('Bienvenue dans votre service astrologique')
try:
	a=int(input("Veuillez saisir votre age"))	
except ValueError:
	print("Attention. Vous n'avez pas saisi une valeur correct. Veuillez recommencer")
except ZeroDivisionError:
	print("La division par zéro sera possible sur Mars. Courage à Thomas Pesquet")
except:
	print("Des erreurs sont survenues. Veuillez réessayer plutard")
else:
	b=randint(1,4)
	c=a*b
	print(f"Vous allez mourir à {c} ans")
finally:
	print("Aurevoir. Le Genie vous remercie")
