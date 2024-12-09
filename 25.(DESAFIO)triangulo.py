print("Digite o comprimento de 3 lados, para validarmos se é um triângulo")
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

if (a < b + c) and (b < c + a) and (c < a + b):
    print("é um triângulo")
else:
    print(" Não é um triângulo")
    
 