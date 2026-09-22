numeros = [4, 7, 12, 5, 18, 3, 22, 9, 15, 6]

# Percorra a lista numeros com for. 
# Quando encontrar o número 18, 
# imprima "Encontrei o 18!" e use break. Antes disso, imprima cada número.

for i in numeros:
    if i == 18:
        print('Encontrei o 18')
        break
    print(i)