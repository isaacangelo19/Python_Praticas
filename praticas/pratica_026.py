
# O que fazer:

# Percorra o dicionário.
# Para cada aluno, calcule a média.
# Se a média for maior ou igual a 7, imprima [nome] APROVADO com média [média].
# Se a média for entre 5 e 6.9, imprima [nome] RECUPERAÇÃO com média [média].
# Se a média for menor que 5, imprima [nome] REPROVADO com média [média].
        
notas = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Carlos": [6, 7, 8],
    "Ana": [9, 9, 10],
    "Pedro": [5, 6, 4]
}
media = 0
for aluno, nota  in notas.items():
    media_aluno = sum(nota)/len(nota)
    print(f'{aluno} : {media_aluno:.2f}')