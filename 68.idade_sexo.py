c = 1 #contador
sexo = str
qnt_mulher = 0
soma_peso_mulher = 0
homem_mais_100 = 0
maior_peso_homem = 0

for c in range (1, 9):
    peso = int(input(f"Digite o peso da {c}º pessoa: "))
    sexo = (input("Homem ou Mulher ? h/m : "))

    if sexo == "m" :
        qnt_mulher += 1
        soma_peso_mulher += peso
    
    if sexo == "h" :
        if peso > 100:
            homem_mais_100 += 1
        if peso > maior_peso_homem :
            maior_peso_homem = peso

print(f"Mulheres Cadastradas: {qnt_mulher}")
print(f"Homens com mais de 100kg: {homem_mais_100}")
print(f"Média peso entre as mulheres: {soma_peso_mulher//qnt_mulher}")
print(f"Maior peso entre os Homens: {maior_peso_homem}")
