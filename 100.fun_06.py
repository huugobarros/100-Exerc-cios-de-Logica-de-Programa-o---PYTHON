
def media(x, y):
    return (x + y)/2

def situacao(resultado):
    if  5.5 <= resultado <= 6.9:
        return "Está em recuperação"
    elif resultado < 5.5:
        return "Está reprovado"
    else:
        return "Está aprovado"

num1 = float(input("digite a primeira nota: "))
num2 = float(input("digite a segunda nota: "))

ocorencia = media(num1,num2)
print(f"Media: {ocorencia} - {situacao(ocorencia)}") 

        
        
    
    