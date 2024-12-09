a = 1 #contador
par = []
impar = []

while a <= 6 :
    num = int(input(f"digita o {a}ª número: "))
    a += 1
    if num % 2 == 0 :
        par.append(num)
    else:
        impar.append(num)
    
    if a > 6 :
        print(f"Par: {par}")
        print(f"Impar: {impar}")
        
        
    
        
    