import random

a = 1 # contador
num = 0
acima_5 = []
div_3 = []
num_sort = []

while a < 21 :
    num = random.randint(0, 10)
    a += 1
    num_sort.append(num)
    if num > 5 :
        acima_5.append(num)
    if num % 3 == 0 :
        div_3.append(num)
        
if a == 21 :
    print(f"Números sorteados: {num_sort}")
    print(f"Números acima de 5: {acima_5}")
    print(f"Números divisíveis por 3: {div_3}")