#Question 1

def factorielle(n):
    if n <= 1:
        return 1
    else:
        valeur=1
        for i in range(1,n+1):
            valeur=valeur*i
        return valeur

#Question2

def binomial(n,p):
    resultat=0
    if 0<=p<=n:
        resultat = factorielle(n) / (factorielle(p) * factorielle(n-p))
    return resultat

def maxBinomial(n):
    maxi=binomial(n,0)
    for i in range(1,n+1):
        valeur=binomial(n,i)
        if valeur > maxi:
            maxi = valeur
    return maxi

def verifMaxBinomial(n):
    m = n//2
    return maxBinomial(n) == binomial(n,m)

#Exemple
print(f"Calcul du factoriel de 5: {factorielle(10)}")
print()
print(f"Calcul du coef binomial (5 3): {binomial(10,4)}")
print()
print(f"Calcul du max des coef binomial de 0 à 5: {maxBinomial(10)}")
print()
print(f"Vérification égalité : {verifMaxBinomial(10)}")

