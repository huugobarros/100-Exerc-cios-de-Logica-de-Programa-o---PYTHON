import random

vet = []
entr = 0

for a in range(30):
    num = random.randint(1, 16)
    vet.append(num)
    
print(vet)

entr = int(input(" digite o valor a ser encontrado no vetor: "))
print(" Valor digitado está nas posições: ")
for a in range(30):
    if vet[a] == entr :
        print(f"{a}")





    