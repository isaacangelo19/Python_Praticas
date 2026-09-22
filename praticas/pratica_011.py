#Crie uma lista com 5 nomes de cidades. U
# se enumerate para imprimir cada cidade no formato:


# 1 - São Paulo
# 2 - Rio de Janeiro
# ...

cidades = ['São Paulo', 'Rio de Janeiro', 'Fortaleza', 'Teresina', 'Belo Horizonte']

for i, cidade in enumerate(cidades, start= 1):
    print(f'{i} - {cidade}')