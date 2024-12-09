first_num = int(input("Digite o primeiro número: ")) #10
end_num = int(input("Digite o ultimo número: ")) # 5
incr = int(input("Digite o número incremental: "))
aux: 0

if first_num > end_num :
    aux = first_num # aux = 10 , first_num = 10
    first_num = end_num # first_num = 5, end_num = 5
    end_num = aux # end_num = 10 , aux = 10
    
    #first_num = 5 , end_num = 10
    

while first_num < end_num :
    print(first_num)
    first_num = first_num + incr
    if first_num >= end_num :
        print("Acabou !")    