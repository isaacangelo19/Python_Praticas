produtos = {
    "arroz": 25.90,
    "feijão": 8.50,
    "macarrão": 4.75,
    "óleo": 7.20,
    "açúcar": 5.30
}

# 1. Lista de compras com preços
# Crie um dicionário com 5 produtos e seus respectivos preços. 
# Depois, mostre na tela cada produto junto com seu preço, um por linha.

for produto, preco in produtos.items():
    print(f'{produto} : {preco:.2f}')