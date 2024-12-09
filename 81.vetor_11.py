idades = []
maior_25 = []
soma_idades = 0
velho = 0
velhos =[]


for a in range(8):
    num = int(input(f"Digite a idade: "))
    idades.append(num)
    soma_idades += num
    if num > 25:
        maior_25.append(a)
    if num > velho :
        velho = num

for a in range(8):
    if idades[a] == velho:
        velhos.append(a)


print(f"Media das idades: {soma_idades/8}")
print(f"Posiçoes maiores que 25: {maior_25}")
print(f"Maior idade digitada: {velho}")
print(f"Posições dos mais velhos: {velhos}")
        
      