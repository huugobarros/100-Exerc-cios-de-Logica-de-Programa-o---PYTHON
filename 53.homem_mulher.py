a = 1 # contador
homem_cad = 0
mulher_cad = 0
soma_idade = 0
mulher_acima_20 = 0
soma_idade_homem = 0

def dividir(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "não há dados para gerar essa informação"

while a < 6 :
    idade = int(input(f"Digite a idade da {a}ª pessoa: "))
    sex = int(input(f"Homem - 1 , Mulher - 2 : "))
    soma_idade += idade
    a += 1
    
    if sex == 1 :
        homem_cad += 1
        soma_idade_homem += idade
    elif sex == 2 :
        mulher_cad += 1
        if idade > 20 :
            mulher_acima_20 += 1
    else: 
        print("Erro")

if a >= 6 :
    media = soma_idade / 5
   
    print(f"Homens Cadastrados: {homem_cad}")
    print(f"Mulheres Cadastradas: {mulher_cad}")
    print(f"Media idade grupo: {media}")
    print(f"Media idade Homens: {dividir(soma_idade_homem, homem_cad)}")
    print(f"Mulheres acima de 20: {mulher_acima_20}")
    
    
    
    
    
    