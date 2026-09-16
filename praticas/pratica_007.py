# Crie um dicionário onde as chaves são nomes de alunos e os valores são listas de notas.
# Exemplo:
# {
#     "João": [7, 8, 9],
#     "Maria": [10, 9, 8],
#     "Carlos": [6, 7, 8]
# }
# Use um for para percorrer o dicionário e calcular a média de cada aluno. 
# Imprima o nome e a média.

notas = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Carlos": [6, 7, 8]
}

print(notas.items())
for i, y in notas.items():
    media = sum(y)/ len (y)
    print(f"{i} : {media}")