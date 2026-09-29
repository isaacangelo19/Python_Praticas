# python

# O que fazer:

# Percorra as vendas.
# Calcule o subtotal de cada venda (quantidade × preço).
# Use um dicionário para acumular o total por produto.
# No final, imprima o total de cada produto e o total geral.
# Saída esperada:

# text
# Camiseta: R$ 249.50
# Calça: R$ 269.70
# Tênis: R$ 199.90
# Total geral: R$ 719.10

vendas = [
    {"produto": "Camiseta", "quantidade": 2, "preco": 49.90},
    {"produto": "Calça", "quantidade": 1, "preco": 89.90},
    {"produto": "Camiseta", "quantidade": 3, "preco": 49.90},
    {"produto": "Tênis", "quantidade": 1, "preco": 199.90},
    {"produto": "Calça", "quantidade": 2, "preco": 89.90}
]


for venda in vendas:
    subtotal = venda['preco'] * venda['quantidade']
    print(f'{venda['produto']} : {subtotal}')