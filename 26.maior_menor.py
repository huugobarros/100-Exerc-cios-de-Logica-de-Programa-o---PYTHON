n1 = int(input("digita um número "))
n2 = int(input("digite outro número "))

if n1 > n2:
    print(f"o primeiro número ({n1}) é maior que o segundo número ({n2}) ")
elif n1 < n2:
    print(f"o primeiro número ({n1}) é menor que o segundo número ({n2}) ")
else:
    print("ambos são iguais")