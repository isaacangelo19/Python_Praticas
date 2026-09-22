

# Percorra a lista numeros e imprima apenas os números pares. 
# Os ímpares devem ser ignorados.

# Saída esperada: 4, 12, 18, 22, 6

numeros = [4, 7, 12, 5, 18, 3, 22, 9, 15, 6]

for i in numeros:
    if i % 2 != 0:
        continue
    print(i)