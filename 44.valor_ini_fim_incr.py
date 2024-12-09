first_num = int(input("Digite o primeiro número: "))
end_num = int(input("Digite o ultimo número: ")) 
incr = int(input("Digite o número incremental: "))

while first_num < end_num :
    print(first_num)
    first_num = first_num + incr
    if first_num == end_num :
        print("Acabou !")    
