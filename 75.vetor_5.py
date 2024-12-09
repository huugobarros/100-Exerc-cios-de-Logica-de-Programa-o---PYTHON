vet = []
p1 = 0
p2 = 0
p3 = 0

for a in range(16):
    if p1 == 0 and p2 == 0 and p3 == 0:
        p3 = 1
        vet.append(p3)
    p1 = p2
    p2 = p3
    p3 = p1 + p2
    vet.append(p3)

for a in range(16):
    print(f"{vet[a]} {a}")
    