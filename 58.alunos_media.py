c = 1 #contador
soma_idade = 0
aluno = 0

while aluno != 999 :
    aluno = int(input(f"qual a idade do {c}º aluno ? "))
    soma_idade += aluno
    if aluno == 999 :
        print(f" quantidade de alunos: {c - 1}")
        print(f" media da idade dos alunos: {(soma_idade - 999 )/(c - 1)}") 
    c += 1



