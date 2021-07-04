'''

	La gestion des exceptions se fait avec les blocs suivants:

		try:
			#On y mettra toutes les instructions susceptibles de générer une exception
		except classeException1:
			#Traitement en cas d'exception appartenant à la classe classeException
			Noous pouvons avoir plusieurs excpet
		except:
			#L'except sans classe d'exception est celle par défuat permettat de capter tous erreurs non gérés

		else:
			#Les instructions qui seront executés s'il n'ya pas d'execption
		finally:
			#Les instructions qui seront executés quelque soit le résultat
	

	raise classeException: permet de lancer une exception
'''


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
