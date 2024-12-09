

a1 = int(input("Digite o primeiro Termo da P.A: ")) 
r = int(input("Razão da P.A: "))

soma = 0
num_ele = 11

if r < 0 :
    num_ele = -11

for a in range(10): 
    print(a1, end=" ")
    soma += a1
    a1 += r
        
print("")
print(f"soma da P.A: {soma} ")
    



 
 