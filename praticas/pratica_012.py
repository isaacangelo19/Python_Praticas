# Crie duas listas: uma com 5 nomes de produtos e outra com 5 preços. 
# Use zip para percorrer as duas ao mesmo tempo e imprimir:

# text
# Produto: Camiseta | Preço: 49.90
# Produto: Calça | Preço: 89.90
# ...

produtos = ['PS5', 'MACBOOK M5', 'IPAD', 'TV 40 Polegadas']
precos = [4500, 8000, 3500, 2000]

for produto, preco in zip(produtos, precos):
    print(f'Produto: {produto.title()} | Preço: {preco:.2f}')