distKm = float(input("quantos KM o carro percorreu ? "))
dias = float(input("quantos dias passou com o carro ? "))

dia_aluguel = dias * 90
km_aluguel = distKm * 0.20

print("Valor por dias alugados: R$",dia_aluguel)
print("Valor por KM rodados: R$",km_aluguel)

total = dia_aluguel + km_aluguel

print("O total do aluguel custa: R$",total)
