def Maior(a, b, c):
    maior = a
    
    if b > maior:
        maior = b
    
    if c > maior:
        maior = c
    
    return maior

resultado = Maior(5, 2, 10)

print(f"O maior número é {resultado}")


