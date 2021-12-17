def est_multiple_7(n):
    if (n == 7 or n == 49):
        return True
    elif (n<7):
        return False
    else:
        u = n%10
        m = n//10
        N = m + 5*u
        print(f'{m} + 5 x {u} = {N}')
        return est_multiple_7(N)

n=490
print(est_multiple_7(n))