from test import division, TestError

try:
    a=int(input("Donner a: "))
    b=int(input("Donner b: "))
    c=division(a,b)
except ValueError:
    print("La valeur saisie ne peut être converti en enntier pour l'opération")
except TestError:
    print("Attention, vous utilisez une variable inexistante")
except ArithmeticError:
        print("La division par Zéro n'est pas autorisée")
#except:
#    print("Des erreurs sont survenus lors du process")
else:
    print(f"{a}/{b} = {c}")
finally:
    print("Fin de programme")