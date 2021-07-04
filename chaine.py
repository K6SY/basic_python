'''
	(*) Les chaines sont définies en utilisant des quotes simples (') ou des quotes doubles (")

	(*) les fonctions générales s'appliquent à plusieurs types d'objets:
		- len : renvoyer la longueur d'un élément
		- del : supprimer un élément
		- Syntaxe: fonction_generale(element)

	(*) Les fonction spécifiques s'appliquent à un type particulier
		- Pour les chaines:
			* upper: Mettre en majuscules
			* lower: mettre en miniscules
		- Syntaxe: element.fonction_specifique(parametre)

	 Exemple:
	 	chaine = 'Bonjour'
		chaine1 = "Bonjour"

	_____________________________
	| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
	_____________________________
	| B | o | n | j | o | u | r |
	_____________________________
	|-7 |-6 |-5 |-4 |-3 |-2 |-1 |
	_____________________________


	(*) Accès aux caractères d'une chaine: 
		- chaine[indice]

'''


chaine1="Bonjour. Nous sommes entrain de voir les chaines des caractères"

chaine='Le responsable est responsable.'

'''
#L'opérateur IN permet de tester l'apartenance d'u caractère/mot/groupe de mot dans une chaine

print('f' in chaine2)

print('e' in chaine1)

#Capitalize: mettre le premier caratère en majuscule et tout le reste en miniscule

str_maj="JE SUIS EN MAJUSCULE"

str_cap=str_maj.capitalize()

print('Capitalize and Maj |-----> ',str_cap, 'vs', str_maj)

#Lower : mettre une chaine en miniscule
str_lower=str_maj.lower()
print('Min and Maj |-----> ',str_lower, 'vs', str_maj)

#Upper: mettre une chaine en majuscule
str_upper=str_cap.upper()
print('maj and Cap |-----> ',str_upper, 'vs', str_cap)


#Endswith and Startswith: permettent de vérifier si une chaine se termine par ou commence par un mot

a = input("merci de saisir un mot commençant par << tr >> et se terminant par << er >")

if a.endswith("er") and a.startswith("tr"):
	print("Bingo. {} respecte la syntaxe requise".format(a))
else:
	print("Vous avez surement sommeil") 

'''

n = len(chaine)

'''	
	la fonction len permet de récuperer la longueur de la chaine

	Les caractères d'une chaine sont indicés:
		(*) positivement de 0 à n-1 (n étant la longueur de la chaine) de la gauche vers la droite
		(*) négativement de -1 à -n (n étant la longueur de la chaine) de la droite vers la gauche

	Pour accéder à un caractère, chaine [indice]
'''
print(f"chaine2 a une taille de {n} caractères, dont le premier est << {chaine[0]} >> et le dernier est << {chaine[n-1]} >>")

print(chaine[-1])

#1ere technique de parcours d'une chaine

for i in range(0,n):
	print(f'le caractère {chaine[i]} est à la position {i+1} ')


#2e technique

for i in chaine:
        print(f'{i}',end=' ** ')


#Sous-chaine

'''
    sc = chaine [start: stop: step]

'''

chaine="Seminaire Python ISI"

#Sous-chaine   avec  start - stop. steppar défaut vaut  1
sc1=chaine[0:9]
#print(sc1)

#Sous-chaine avec  start - stop - step
sc2=chaine[0:9:2]
#print(sc2)

#Omission du start - Si on commence par 0
sc3=chaine[:9]
#print(sc3)

#Omission du stop - Si on termine à la fin
sc4=chaine[9:]
print(sc4)

#Inversion chaine
ci=chaine[::-1]
print(ci)
