nomes =[]
cont = 1

for a in range(1, 8):
    nome = input(f"Digite o {a}º nome: ")
    nomes.append(nome)

for a in range(6, -1, -1):
   print(f" {cont}º Nome: {nomes[a]}")
   cont += 1
   