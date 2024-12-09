a = 1 #contador
preco = float
maior_num = 0
menor_num = 99999

while a < 9 :
    preco = float(input(f"qual o valor do {a}º Produto: "))
    a += 1
    if preco > maior_num :
        maior_num = preco
    if preco < menor_num :
        menor_num = preco

if a == 9 :
    print(f"maior preço: {maior_num}")
    print(f"menor preço: {menor_num}")
    