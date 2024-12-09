def Maior(x, y):
    if x > y:
        print(f"{x} é maior que {y}")
    elif x < y:
        print(f"{y} é maior que {x}")
    else:
        print(f"{x} e {y} são iguais")

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))

Maior(num1,num2)
