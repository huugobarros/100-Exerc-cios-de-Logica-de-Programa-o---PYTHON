
cont1 = 0
cont2 = 0

def selecao_jogo ():
    global cont1
    global cont2

    print("Player 1 : 1 - Pedra")
    print("         : 2 - Papel")
    print("         : 3 - Tesoura")
    p1 = int(input())

    print("Player 2 : 1 - Pedra")
    print("         : 2 - Papel")
    print("         : 3 - Tesoura")
    p2 = int(input())

    if (p1 == 1 and p2 == 1) or (p1 == 2 and p2 == 2) or (p1 == 3 and p2 == 3) :
        print("EMPATE")
    elif (p1 == 1 and p2 == 2): #p1 = pedra , p2 = papel -> p2 ganha
        cont2 = cont2 + 1    
    elif (p1 == 1 and p2 == 3): #p1 = pedra , p2 = tesoura -> p1 ganha
        cont1 = cont1 + 1
    elif (p1 == 2 and p2 == 1): #p1 = papel , p2 = pedra -> p1 ganha
        cont1 = cont1 + 1
    elif (p1 == 2 and p2 == 3): #p1 = papel , p2 = tesoura -> p2 ganha
        cont2 = cont2 + 1
    elif (p1 == 3 and p2 == 1): #p1 = tesoura , p2 = pedra -> p2 ganha
        cont2 = cont2 + 1
    else: #p1 = tesoura , p2 = papel -> p1 ganha
        cont1 = cont1 + 1



while cont1 != 3 or cont1 != 3:
    selecao_jogo()
    print("---------Placar---------")
    print("Player1 {} X {} Player2".format(cont1,cont2))
    

    if cont1==3 or cont2==3:    
        print("")
        print("------FIM DE JOGO------")
        exit()


