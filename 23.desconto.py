nome = input("qual o seu nome ?")
sex = int(input("você é homem ou mulher ? homem-1/ Mulher-2"))
valor = float(input("valor da compra ? "))

if sex == 1:
    desc = valor - (valor * 5/100)
    print("{}, o total da sua compra com desconto de 5%: R${}".format(nome,desc))
elif sex == 2:
    desc = valor - (valor * 13/100)
    print("{}, o total da sua compra com 13%: R${}".format(nome,desc))
else:
    print("Informe o seu sexo corretamente.")


