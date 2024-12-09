
# dados de entrada
casa_valor = float(input("Qual o valor da casa a ser comprada ? ")) #30.000,0
salario = float(input("Qual o seu salário ?")) #3.000
ano_parcela = int(input("em quantos anos deseja parcelar ?")) # 2

#operações
mes_parcela_qnt = ano_parcela * 12 # 24
cond = salario * (30/100) #900
parcela_mensal = casa_valor / mes_parcela_qnt #30.000.0 / 24

if parcela_mensal > cond :
    print("Emprestimo Negado !") #este será o resultado. 
else:
    print("Emprestimo Aprovado !")









