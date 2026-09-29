produtos = {
    "arroz": 25.90,
    "feijão": 8.50,
    "macarrão": 4.75,
    "óleo": 7.20,
    "açúcar": 5.30
}

# 2. Soma dos valores
# Usando o dicionário do exercício anterior, 
# calcule e mostre o valor total da compra (soma de todos os preços).
valor_total = 0
for produto, preco in produtos.items():
    valor_total += preco
print(f'Preço Total: {valor_total:.2f}')