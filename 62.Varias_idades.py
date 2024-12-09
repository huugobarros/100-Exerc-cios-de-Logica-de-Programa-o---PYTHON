
flag = "s"
a = 1 # contador
soma_idade = 0
mais_21_cont = 0


while True:
    idade = int(input(f"digite a idade da {a}º pessoa: "))
    flag = input("Deseja continuar ? s/n : ")
    soma_idade += idade
    
    if idade >= 21:
        mais_21_cont += 1
     
    
    if flag == "n":
        print(f"idades digitada: {a} ")
        print(f"Media das idades: {soma_idade/a}")
        print(f"idades 21 ou mais: {mais_21_cont}")
        break
    a += 1
    
