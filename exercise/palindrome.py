def palindrome(mot):
    mot_inverse=mot[::-1]
    print(mot_inverse)
    return mot == mot_inverse

m=input("Veuillez saisir un mot?\t")

resultat=palindrome(m)

reponse=f"{m} est un palindrome"

if resultat:
    print(reponse)
else:
    reponse = reponse.replace("est","n'est pas")
    print(reponse)