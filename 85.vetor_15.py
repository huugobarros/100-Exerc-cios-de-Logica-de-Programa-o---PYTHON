nomes = []
sexos = []
salarios = []

for a in range(5):
    nome = input("Nome: ")
    nomes.append(nome)
    
    sexo = input("Homem ou Mulher ? h/m : ")
    sexos.append(sexo)
    
    salario = int(input("Salario: "))
    salarios.append(salario)

print("Lista de mulheres que recebem mais que 5k: ")
for a in range(5):
    if sexos[a] == "m":
        if salarios[a] > 5000:
            print(f"{nomes[a]}")
            
    