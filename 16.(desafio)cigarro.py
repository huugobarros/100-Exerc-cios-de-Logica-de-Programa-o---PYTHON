cig_dia = int(input("Quantos cigarro fuma por dia ? "))
anos_fuma = int(input(" Fuma a quantos anos ? "))

dias_fuma = anos_fuma * 365 #converte os anos que fuma em total de dias que fuma.
total_cig_anos = cig_dia * dias_fuma #total de cigarros fumados durante os anos informados.

perda_total_minutos = total_cig_anos * 10 #total dos minutos perdidos

perda_total_dia = perda_total_minutos //1440 #convertendo minutos em dias

print("Ja perdeu {}dias ".format(perda_total_dia))






