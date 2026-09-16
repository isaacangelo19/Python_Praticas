# Crie um dicionário com os dados de um aluno: nome, idade, curso, nota. 
# Use um for para percorrer o dicionário e imprimir cada chave e seu valor no formato:
# nome: João
# idade: 22
# curso: Engenharia
# nota: 8.5

aluno = {
    'nome' : 'isaac angelo mota',
    'idade' : 24,
    'curso' : 'formado',
    'nota' : 7
}

for c, v in aluno.items():
    print(f"{c} : {v}")
    