vet = []

for a in range(10):
    if a % 2 != 0:
        vet.append(3)
    else:
        vet.append(5)

for a in range(10):
    print(f"{vet[a]}  {a}")