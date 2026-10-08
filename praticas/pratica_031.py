notas = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carla": 9.2,
    "Diego": 7.8
}

# Crie um dicionário com o nome de 4 alunos e suas notas. Mostre:

# cada aluno e sua nota
# a média da turma
# o nome do aluno com a maior nota
soma_nota = 0
for aluno, nota in notas.items():
    print(f'{aluno} : {nota}')
    soma_nota += nota

media = soma_nota/len(notas.keys())
print(f'A média foi {media:.2f}')
