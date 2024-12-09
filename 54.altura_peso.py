a = 1 # contador
acima_90 = 0 #contador de pessoas com peso acima de 90kg
soma_altura = 0
abaixo_50_abaixo_160 = 0
acima_100_acima190 = 0


while a < 8 :
    peso = int(input(f" digite peso da {a}º pessoa: "))
    altura = float (input(f"digite a altura em metros da {a}º pessoa: "))
    soma_altura += altura
    a += 1
    
    if peso > 90 :
        acima_90 += 1
    if peso < 50 and altura < 1.60 :
        abaixo_50_abaixo_160 += 1
    if altura > 1.90 and peso > 100 :
        acima_100_acima190 += 1
        
if a > 7 :
    print(f" Média da altura do grupo: {soma_altura//7}")
    print(f" Pessoas acima de 90kg: {acima_90}")
    print(f" Pessoas abaixo de 50kg e 1.60m de altura: {abaixo_50_abaixo_160}")
    print(f" Pessoas acima de 1.90m de altura e 100kg: {acima_100_acima190}")
    
    
    


