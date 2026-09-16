# Crie uma lista com 3 dicionários. 
# Cada dicionário representa um produto com nome e preco. 
# Use um for para percorrer a lista e imprimir o nome e o preço de cada produto.

dicionarios = [
    {
        'PS5' : 4500
    },
    {
        'Macbook': 7000
    },
    {
        'Ipad' : 3000
    }
]


for i in dicionarios:
    for chave, valor in i.items():
        print(i.items())

# Usando a lista do exercício anterior, 
# use um for para imprimir apenas os produtos com preço maior que 50.

for i in dicionarios:
    for chave, valor in i.items():
        if valor > 5000:
            print(f'{chave} : {valor}')