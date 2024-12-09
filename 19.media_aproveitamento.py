n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = float ( n1 + n2 ) / 2

if media > 7 :
    print("Media: {}, Aluno possui bom aproveitamento".format(media))
else:
    print("Media: {}, Aluno não teve bom aproveitamento.".format(media))