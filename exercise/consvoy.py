
voyelle="aeiouy"

chaine=input("Veuillez saisir une chaine de caractères \n")

n = len(chaine)

#tranformation en miniscule
chaine = chaine.lower()

cpt_voy=0
cpt_cons=0

for i in chaine:
	if i.isalpha():
		if i in voyelle:
			cpt_voy+=1
		else:
			cpt_cons+=1

print(f"La chaine que vous avez saisie est constituée de {n} caractères dont {cpt_voy} voyelles, {cpt_cons} consonnes et { n - cpt_voy - cpt_cons} caractètes non alphabétiques")

