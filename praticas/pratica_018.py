

# Percorra a lista numeros e vá somando os valores em uma variável. 
# Imprima cada número somado. 
# Quando a soma ultrapassar 50, imprima "Limite atingido!" e pare a repetição.

numeros = [4, 7, 12, 5, 18, 3, 22, 9, 15, 6]

valor_total = 0
for numero in numeros:
    valor_total += numero
    if valor_total >= 50:
        print('Limite atingido!')
        break
    print(f'número {numero} somado ao valor_total')
