
# Usando a lista de preços do exercício anterior, 
# percorra com for e imprima apenas os produtos com preço maior que 4000. 
# Use zip para associar nome e preço.


produtos = ['PS5', 'MACBOOK M5', 'IPAD', 'TV 40 Polegadas']
precos = [4500, 8000, 3500, 2000]

for produto, preco in zip(produtos, precos):
    if preco >= 4000:
        print(f'Produto: {produto.title()} | Preço: {preco:.2f}')