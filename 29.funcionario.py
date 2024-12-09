nome_fun = input("Qual o nome do funcionário ?")
salario_fun = float(input("qual o seu salário ?"))
anos_trab = int(input("quantos anos trabalha ?"))

antigo_sal = salario_fun

if anos_trab <= 3 :
    salario_fun = salario_fun + (salario_fun * 3/100)
elif anos_trab > 3 and anos_trab < 10 :
    salario_fun = salario_fun + (salario_fun * 12.5/100)
else:
    salario_fun = salario_fun + (salario_fun * 20/100)

print (f"trabalhador {nome_fun} trabalha a {anos_trab} anos, com o salário de R${antigo_sal}, agora com o aumento seu salario é {salario_fun}")