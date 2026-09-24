# Contexto: Você tem um snapshot antigo e um snapshot novo de uma tabela de produtos. 
# Precisa detectar o que mudou.

# Estrutura:

# python

# O que fazer:

# Loop externo: percorra os produtos do snapshot_novo.
# Loop interno: percorra os produtos do snapshot_antigo.
# Se o id for igual:

# Compare cada campo (nome, preco).
# Se algum campo for diferente, imprima [id] MUDOU: [campo] de [antigo] para [novo].
# Se nenhum campo mudou, imprima [id] SEM MUDANÇA.
# Se o id do novo não existir no antigo, imprima [id] NOVO PRODUTO.
# Saída esperada:

# text
# 1 MUDOU: preco de 49.90 para 59.90
# 2 SEM MUDANÇA
# 4 NOVO PRODUTO

snapshot_antigo = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
    {"id": 2, "nome": "Calça", "preco": 89.90},
    {"id": 3, "nome": "Tênis", "preco": 199.90}
]

snapshot_novo = [
    {"id": 1, "nome": "Camiseta", "preco": 59.90},  # preço mudou
    {"id": 2, "nome": "Calça", "preco": 89.90},     # sem mudança
    {"id": 4, "nome": "Boné", "preco": 29.90}       # novo produto
]

for antigo, novo in zip(snapshot_antigo, snapshot_novo):
    if antigo['nome'.lower()] == novo ['nome'.lower()] and antigo['preco'.lower()] != novo['preco'.lower()]:
        print(f'id {antigo['id']} mudou de preço de {antigo['preco'.lower()]} para {novo['preco'.lower()]}')
    else:
        print(f'id {antigo["id"]} SEM MUDANÇA')
    for i, x in zip(antigo["id"], novo['id']):
        print(i,x)