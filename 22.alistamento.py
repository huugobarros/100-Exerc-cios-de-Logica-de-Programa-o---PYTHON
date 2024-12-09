ano = int(input("qual seu ano de nascimento?"))
idade = 2024 - ano

if idade < 18:
    print("Falta {} anos para o alistamento".format(18 - idade))
else:
    print("fazem {} anos que você pode se alistar".format(idade - 18))
    