
a = 1 #contador
soma = 0
num = 0


while num != 1111 :
    num = int(input(f"Digite o {a}º Número"))
    soma += num

if num == 1111 :
    print("erro número 1111")
    
else:
    print("Soma:{}".format(soma))
