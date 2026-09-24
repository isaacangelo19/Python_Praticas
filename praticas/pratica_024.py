
# Regras de validação:

# O nome não pode ser vazio.
# O salario tem que ser maior que 0.
# O departamento só pode ser "TI", "RH", "Financeiro" ou "Diretoria".
# O que fazer:


# Total de aprovados e rejeitados.
# Salário total dos aprovados.
# Salário médio dos aprovados.
# Saída esperada:

# text
# Funcionário 2: nome vazio
# Funcionário 3: salário inválido
# Funcionário 5: salário inválido

# Aprovados: 3 | Rejeitados: 3
# Salário total: R$ 17500.00
# Salário médio: R$ 5833.33


funcionarios = [
    {"id": 1, "nome": "João", "salario": 5000.00, "departamento": "TI"},
    {"id": 2, "nome": "", "salario": 3000.00, "departamento": "RH"},
    {"id": 3, "nome": "Carlos", "salario": -1000.00, "departamento": "TI"},
    {"id": 4, "nome": "Ana", "salario": 4500.00, "departamento": "Financeiro"},
    {"id": 5, "nome": "Pedro", "salario": 0.00, "departamento": "TI"},
    {"id": 6, "nome": "Maria", "salario": 8000.00, "departamento": "Diretoria"}
]

aprovados = 0
reprovados = 0
folha_salarial = 0
folha_salarial_media = 0

for funcionario in funcionarios:
    erro = False
    if funcionario['nome'] == '':
        erro = True
        print(f'O id {funcionario['id']} está com nome vazio')
    if funcionario['salario'] <= 0:
        erro = True
        print(f'O id {funcionario["id"]} está com salário errado')
    if funcionario['departamento'] not in ["TI", "RH", "Financeiro","Diretoria"]:
        erro = True
        print(f'O id {funcionario["id"]} está com erro de departamento')
    if erro == True:
        reprovados += 1
    else: aprovados += 1
    if erro == False:
        folha_salarial += funcionario["salario"]
        folha_salarial_media = (folha_salarial)/ aprovados

print(f''' Aprovados : {aprovados} | Reprovados : {reprovados}
        Folha salarial : {folha_salarial} | Folha salarial média {folha_salarial_media:.2f}
''')
    