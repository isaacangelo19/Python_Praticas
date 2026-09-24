# Exercício 1 — Validação de dados em lote (staging → final)

# Contexto: Você recebeu uma lista de registros de clientes que precisam ser 
# validados antes de entrar no banco. Cada registro é um dicionário. 
# Você precisa percorrer cada registro e validar campo por campo.

# Estrutura:

# python

# O que fazer:

# Loop externo: percorra cada registro.
# Loop interno: percorra cada campo (chave) do registro.
# Para cada campo, valide:

# Se nome estiver vazio → imprima [id] ERRO: nome vazio.
# Se email não contiver @ → imprima [id] ERRO: email inválido.
# Se idade for menor que 0 ou maior que 120 → imprima [id] ERRO: idade inválida.
# Se o registro tiver qualquer erro, marque como REJEITADO.
# Se não tiver erro, imprima [id] APROVADO.
# Saída esperada:
# text
# 1 APROVADO
# 2 ERRO: nome vazio
# 2 APROVADO
# 3 ERRO: email inválido
# 3 ERRO: idade inválida
# 3 APROVADO
# ...

registros = [
    {"id": 1, "nome": "João", "email": "joao@email.com", "idade": 22},
    {"id": 2, "nome": "", "email": "maria@email.com", "idade": 20},
    {"id": 3, "nome": "Carlos", "email": "carlos_email_invalido", "idade": -5},
    {"id": 4, "nome": "Ana", "email": "ana@email.com", "idade": 25},
    {"id": 5, "nome": "Pedro", "email": "", "idade": 0}
]

for registro in registros:
    if registro['nome'] == '':
        print(f'{registro['id']} ERRO: nome vazio. REJEITADO')
    # Se email não contiver @ → imprima [id] ERRO: email inválido.
    elif '@' not in registro['email']:
        print(f'{registro['id']} ERRO: email invalido. REJEITADO')
    # Se idade for menor que 0 ou maior que 120 → imprima [id] ERRO: idade inválida.
    elif registro['idade'] < 0 and registro["idade"] > 120:
        print(f'{registro['id']} ERRO: idade invalida. REJEITADO')
    else:print(f'{registro['id']} APROVADO')
    
            