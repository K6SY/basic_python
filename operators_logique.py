'''
    Les opérateurs logiques que nous avons:

    Et  : and
    Ou  : or
    Non  : not

    True --> 1
    False --> 0
    
    cond1 and cond2

    --------------------------
    | AND  |    1    |    0   |
    ---------------------------
    |  1   |    1    |   0    |
    ---------------------------
    |  0   |    0    |    0   |
    ---------------------------

    --------------------------
    | 0R   |    1    |    0   |
    ---------------------------
    |  1   |    1    |   1    |
    ---------------------------
    |  0   |    1    |    0   |
    ---------------------------

    Not True  ---> False
    Not False ---> True

'''

#Exemple: Année bissextile
# une année est bissextile si l'année est multiple de 4 et non multiple 100
# Ou l'année est multiple de 400

an = int(input('Merci d\'indiquer une année \t'))

cond1 = an%4 == 0
cond2 = an%100 != 0  # cond2 = not(an%100 == 0)
cond3 = an%400 == 0

bissextile = (cond1 and cond2) or cond3

print(f"L'année {an} est bissextile: {bissextile}")
