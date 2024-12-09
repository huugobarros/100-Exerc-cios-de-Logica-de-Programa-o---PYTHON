import random
vet = []

for a in range(10):
    num = random.randint(1, 11)
    vet.append(num)

print(vet)
print("Posição dos valores pares: ")
for a in range(len(vet)):
    if vet[a] % 2 == 0 :
        print(f"{a}")
    