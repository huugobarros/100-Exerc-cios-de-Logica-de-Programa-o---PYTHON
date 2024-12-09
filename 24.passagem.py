dist = float(input("qual distancia vai percorrer em km ?"))

if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.50
    
print(" O valor da viagem custará: R$ ",valor)


