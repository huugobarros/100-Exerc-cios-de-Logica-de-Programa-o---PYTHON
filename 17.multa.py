velo = float(input("qual a velocidade ?"))
a = 0

if velo > 80 :
    print("você foi multado")
    a = velo - 80   
    multa = a * 5
    print("Sua multa custa: R$",multa) 
else:
    print(" velocidade permitida !")



    