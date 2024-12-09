
c = 1 # contador
maior_idade = 0
h_cadas = 0
mulher_jovem = 9999

soma_idade_h = 0

flag = "s"

while flag == "s" :
    idade = int(input(f"Qual a idade da {c}º pessoa ?"))
    sex = str(input("homem ou mulher ? h/m"))
      
    if sex == "h" :
        h_cadas += 1
        soma_idade_h += idade
    if sex == "m" :
        if idade < mulher_jovem:
            mulher_jovem = idade
    if idade > maior_idade:
        maior_idade = idade
    
    c += 1
    flag = str(input("deseja continuar ? s/n "))

print(f" Maior idade registrada: {maior_idade}")
print(f"Quantidade de homens cadastrados: {h_cadas}")
print(f"Idade da mulher mais jovem: {mulher_jovem}")
print(f"media de idade entre os homens: {soma_idade_h / h_cadas}")
        