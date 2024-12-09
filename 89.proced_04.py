def gerador(nome, repet, bord):
    if bord == 1 :
        borda = "+-------=======------+"
    if bord == 2 :
        borda = "~~~~~~~~:::::::~~~~~~~"
    if bord == 3 :
        borda = "<<<<<<<<------->>>>>>>"
    
    print(borda)
    
    for a in range(repet):
        print(f"{nome}")
    
    print(borda)

gerador("Aprendendo python", 3, 2)
      
    