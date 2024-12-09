import random

a = 1 #contador
num_vetor = []
num_input = 0
num_randon = random.randint(1, 10)

while a < 11 :
    num_input = int(input(f"Digite o {a}º número: "))
    num_vetor.append(num_input)
    a += 1

if num_randon in num_vetor:
    print(f" número aleatório: {num_randon}, foi digitado ")
else:
    print(f" número aleatório: {num_randon}, não foi digitado ")


print(num_vetor)
    

    
    
    
    






