first_num = 6
soma = 0

while first_num <= 100 :
    print(f"{first_num}")
    soma += first_num
    first_num += 2
    if first_num > 100 :
        print(f"SOMA DE TODOS: {soma}")