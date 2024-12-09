import random

cont = 0

while cont == 0 :
    num_ale = random.randint(1, 5)
    num = int(input("Digite um número"))
    
    if num_ale == num :
        cont = cont + 1
        print(f" Aleatório -> {num_ale} e {num} <- númro digitado, são iguais")
      
    else:
        print(f"{num_ale} e {num} são diferentes")







