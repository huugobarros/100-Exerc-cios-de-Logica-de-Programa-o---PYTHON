a = 1 #contador
soma_idade = 0
maior_18 = 0
menor_5 = 0
idade_maior = 0

while a < 11:
    idade = int(input(f"Digite a idade da {a}ª pessoa: "))
    a += 1
    soma_idade += idade
    if idade > 18 :
        maior_18 += 1
    if idade < 5 :
        menor_5 += 1
    if idade > idade_maior :
        idade_maior = idade
        
if a == 11 :
    print(f"Quantidade de maiores de 18 anos : {maior_18}")
    print(f"Quantidade de menores de 5 anos : {menor_5}")
    print(f"Maior idade: {idade_maior}")
    
    
    
        

