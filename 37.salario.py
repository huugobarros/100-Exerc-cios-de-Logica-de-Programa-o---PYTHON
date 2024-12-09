gen = int(input("homem ou mulher ? 1-Homem , 2-Mulher "))
sal_atual = float(input("Qual o seu salário atual ? R$"))
anos_trab = int(input("Quantos anos trabalha na empresa ? "))

if gen == 1 :
    if anos_trab < 20:
        sal_novo = sal_atual + (sal_atual * 3/100)
    elif anos_trab >= 20 and anos_trab <= 30:
        sal_novo = sal_atual + (sal_atual * 13/100)
    else:
        sal_novo = sal_atual + (sal_atual * 25/100)
else:
    if anos_trab < 15:
        sal_novo = sal_atual + (sal_atual * 5/100)
    elif anos_trab >= 15 and anos_trab <= 20:
        sal_novo = sal_atual + (sal_atual * 12/100)
    else:
        sal_novo = sal_atual + (sal_atual * 23/100)
        
print(f"novo salário: R${sal_novo}")
        
