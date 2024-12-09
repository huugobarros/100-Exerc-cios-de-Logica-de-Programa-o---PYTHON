ano_nascm = int(input("em que ano nasceu ?"))

idade = 2024 - ano_nascm

if idade > 18 :
    print("você possui {} anos, Pode votar !".format(idade))
else:
    print("Você possui {} anos, não pode votar !".format(idade))
