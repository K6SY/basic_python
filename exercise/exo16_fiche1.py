x=int(input("Donner un nombre"))
n=int(input("Donner le nombre de chiffre"))

avoir_n_chiffres = 10**(n-1) <= x < 10**n
print(f"Le nombre {x} est contitué de {n} chiffre (s): {avoir_n_chiffres}")