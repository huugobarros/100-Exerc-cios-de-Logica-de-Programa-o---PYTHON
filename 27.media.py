n1 = float(input("digita a primeira nota "))
n2 = float(input("digita a segunda nota "))

media = (n1 + n2) / 2

if media < 5.0:
    print(f"Média: {media} , REPROVADO")
elif media > 4.9 and media < 7.0 :
    print(f"Média: {media} , RECUPERAÇÃO")
else: 
    print(f"Média: {media} , APROVADO")
    
