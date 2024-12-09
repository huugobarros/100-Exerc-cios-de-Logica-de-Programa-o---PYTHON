base = float(input("digite a base do terreno em metros: "))
altura = float(input("digite a altura do terreno em metros: "))

area = base * altura

if area > 500 :
    print(f"terreno possui {area}m² , TERRENO VIP")
elif area <= 500 and area >= 100 :
    print(f"terreno possui {area}m² , TERRENO MASTER")
else:
    print(f"terreno possui {area}m² , TERRENO POPULAR")