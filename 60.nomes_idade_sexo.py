
flag = "s"
c = 1 #contador

idade_maior = 0
nome_maior = str
soma_idades = 0

#homem
homem_mais_30 = 0

#mulher
mulher_menos_18 = 0
mulher_idade_jovem = 9999
nome_mulher_jovem = str



while flag == "s" :
    nome = str(input(f"Nome da {c}º pessoa: "))
    idade = int(input(f"digite a idade da {c}º pessoa: "))
    sexo = str(input(f"homem ou mulher ? h/m : "))
    
    soma_idades += idade
    
    if idade > idade_maior :
        idade_maior = idade
        nome_maior = nome
    
    if sexo == "h" :
        if idade > 30 :
            homem_mais_30 += 1
        
    if sexo == "m" :
        if idade < mulher_idade_jovem:
            mulher_idade_jovem = idade
            nome_mulher_jovem = nome
        if idade < 18 :
            mulher_menos_18 += 1
    
    c += 1
    flag = str(input("Deseja continuar ? s/n"))

print(f"Nome da pessoa mais velha: {nome_maior}")
print(f"Nome da mulher mais jovem: {nome_mulher_jovem}")
print(f"Media de idade do Grupo: {soma_idades // c}")
print(f"Homens com mais de 30 : {homem_mais_30}")
print(f"Mulheres com menos de 18 : {mulher_menos_18}")

    
    
    

