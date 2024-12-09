c = 1
flag = "s"
soma_num = 0
menor_num = 9999
par_num = 0


while flag == "s":
    num =int(input(f"digite o {c}º número: "))
    soma_num += num
    
    if num < menor_num :
        menor_num = num
    
    if num % 2 == 0 :
        par_num += 1
    
    flag = input("Deseja continuar ? s/n : ")
    if flag == "s" :
        c += 1

print(f"Soma de todos os valores: {soma_num}")
print(f"O menor número digitado: {menor_num}")
print(f"Media dos valores digitados: {soma_num/ c}")
print(f"Quantidade de números pares: {par_num}")