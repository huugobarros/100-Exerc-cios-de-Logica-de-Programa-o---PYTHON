total_sal_homem = 0
total_sal_mulher = 0
flag = str
cont = 0

while cont == 0 :

    salario = int(input("digite o salário: R$ "))
    sex = str(input(" Homem ou Mulher ? h/m : "))

    if sex == "h" :
        total_sal_homem += salario
    if sex == "m" :
        total_sal_mulher += salario

    flag = str(input("Deseja continuar ? s/n "))
    if flag == "s" :
        cont += 0
    if flag =="n" :
        cont += 1

print(f"Total de salário pago aos homens R$ {total_sal_homem}")
print(f"Total de salário pago as mulheres R$ {total_sal_mulher}")
        
        
        
