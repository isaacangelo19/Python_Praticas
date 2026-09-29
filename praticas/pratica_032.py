estoque = {
    "caneta": 50,
    "lápis": 8,
    "borracha": 3,
    "caderno": 12,
    "mochila": 5,
    "régua": 20
}

# 5. Filtrando por condição
# Crie um dicionário com nomes de produtos e suas quantidades em estoque. 
# Mostre apenas os produtos que têm quantidade menor que 10 (abaixo do mínimo).

for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(f'{produto} : {quantidade} abaixo do mínimo')
    else: continue