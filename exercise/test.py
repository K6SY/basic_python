def div (n):
    if n == 1:
        return 0
    else:
        if n%2 != 0:
            n = n+1
        r = n//2
        print(r)
        return 1+div(r)

print(f"Nombre de division: {div(10)}")