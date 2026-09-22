# Crie uma lista com 5 frutas. 
# Use enumerate para criar um dicionário onde a chave é o índice (1, 2, 3...) e o valor é a fruta.

# Resultado esperado:

# text
# {1: 'maçã', 2: 'banana', 3: 'laranja', ...}

frutas = ['maça', 'laranja', 'uva', 'morango', 'pera']


dicionario_frutas = {}

for indice, fruta in enumerate(frutas, start=1):
    dicionario_frutas[indice] = fruta

print(dicionario_frutas)