notas = []
soma_nota = 0
maior_nota = 0
posi_maior = []
acima_media = 0

for a in range(10):
    nota = int(input(f"Digita a nota do aluno: "))
    notas.append(nota)
    soma_nota += nota
    if nota > maior_nota:
        maior_nota = nota
        
for a in range(10):
    if notas[a] == maior_nota:
        posi_maior.append(a)        
        
for a in range(10):
    if notas[a] > (soma_nota/10):
        acima_media += 1

print(f"Media da turma: {soma_nota/10}")
print(f"Número de alunos acima da média: {acima_media}")
print(f"Maior nota: {maior_nota}")
print(f"Posições que a maior nota aparece: {posi_maior}")


    
    



