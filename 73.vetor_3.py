vet = []
c = 9

for a in range(9, -1, -1):
    vet.append(c)
    c-=1

for a in range(10):
    print(f"{vet[a]} {a}")