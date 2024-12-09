print("Que tipo de carro deseja alugar ?")
print("                      1 - popular")
print("                      2 - luxo")
tipo_carro = int(input())
dias_aluguel = int(input("Quantos dias vai alugar? "))
km_percorrido = int(input("Quantos KM percorrido ? "))

if tipo_carro == 1 : # Carro popular 
    dias_corrido_total = dias_aluguel * 90
    if km_percorrido <= 100 :
        total_Km = km_percorrido * 0.20
    else:
        total_Km = km_percorrido * 0.10
        
elif tipo_carro == 2 : #Carro Luxo
    dias_corrido_total = dias_aluguel * 150
    if km_percorrido <= 200 :
        total_Km = km_percorrido * 0.30
    else:
        total_Km = km_percorrido * 0.25
else:
    print(" Opção de carro inválida.")
    
fim_total_aluguel = total_Km + dias_corrido_total
    
print(f"O Valor do aluguel do seu carro : R$ {fim_total_aluguel}")
    

    
    