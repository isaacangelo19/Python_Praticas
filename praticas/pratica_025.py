
# Regras de validação:

# O produto não pode ser vazio.
# O preco tem que ser maior que 0.
# A quantidade tem que ser maior ou igual a 0 (quantidade 0 é válida, mas o produto está esgotado).
# O que fazer:

# Percorra cada produto.
# Use uma flag para rastrear se o produto tem erro.
# Use contadores para somar aprovados e rejeitados.
# Use um acumulador para somar o valor total do estoque (preço × quantidade) dos aprovados.
# Para cada erro, imprima uma mensagem específica.
# Regra extra: se o produto for válido mas a quantidade for 0, imprima [produto] ESGOTADO (mas ainda conta como aprovado).
# No final, imprima:

# Total de aprovados e rejeitados.
# Valor total do estoque.
# Quantos produtos estão esgotados.
# Saída esperada:

# text
# Produto 2: nome vazio
# Produto 3: preço inválido
# Produto 6: quantidade inválida
# Boné ESGOTADO

# Aprovados: 3 | Rejeitados: 3
# Valor total do estoque: R$ 2649.20
# Produtos esgotados: 1

aprovados = 0
reprovados = 0
produtos_esgotados = 0
valor_total_estoque = 0

estoque = [
    {"id": 1, "produto": "Camiseta", "preco": 49.90, "quantidade": 10},
    {"id": 2, "produto": "", "preco": 89.90, "quantidade": 5},
    {"id": 3, "produto": "Tênis", "preco": -199.90, "quantidade": 3},
    {"id": 4, "produto": "Boné", "preco": 29.90, "quantidade": 0},
    {"id": 5, "produto": "Jaqueta", "preco": 299.90, "quantidade": 7},
    {"id": 6, "produto": "Meia", "preco": 19.90, "quantidade": -5}
]

for i in estoque:
    erro = False
    if i['produto'] == '':
        erro = True
        print(f'O id {i['id']} está com o produto vazio')
    if i['preco'] <= 0:
        erro = True
        print(f'O id {i["id"]} está com preço menor que 0')
    if i['quantidade'] < 0:
        erro = True
        print(f'O id {i["id"]} está com a quantidade negativa')
    if erro == True:
        reprovados += 1
    else: aprovados += 1

    if i['quantidade'] == 0:
        produtos_esgotados += 1
        print(f'{i["produto"]} ESGOTADO')
    if erro == False:
        valor_total_estoque = i["preco"] * i["quantidade"]

print('Resumo')
print(f'''Aprovados: {aprovados} | Reprovados: {reprovados}
        Valor total em estoque: {valor_total_estoque:.2f}
        Produtos esgotados: {produtos_esgotados}''')
    