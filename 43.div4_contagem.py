a = 30

while a > 1 :
    if a % 4 == 0 :
        print(f"[{a}]")
    else:
        print(a)
    a -= 1
    
if a == 1:
    print("Acabou!")

