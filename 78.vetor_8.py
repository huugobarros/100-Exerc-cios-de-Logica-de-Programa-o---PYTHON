vet = []

for a in range(15):
    num = int(input("Digite um número: "))
    vet.append(num)
    
print(vet)

print("Posição dos valores divisíveis por 10: ")
for a in range(len(vet)):
    if vet[a] % 10 == 0:
        print(f"{a}")
        
    
    