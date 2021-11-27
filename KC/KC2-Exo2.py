def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n*factoriel(n-1)