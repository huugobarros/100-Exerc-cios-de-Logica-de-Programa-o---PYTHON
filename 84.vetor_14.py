nomes = []
idades = []

for a in range(9):
    nome = input("Digite o nome: ")
    nomes.append(nome)
    idade = int(input("Digite a idade: "))
    idades.append(idade)

print("Lista das pessoas maiores de idade: ")
for a in range(9):
    if idades[a] >= 18 :
        print(f"{nomes[a]} - {idades[a]}")
    
        