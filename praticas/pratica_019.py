# Use um loop externo para percorrer numeros.
# Use um loop interno para percorrer numeros novamente.
# Imprima a multiplicação no formato 1 x 1 = 1.
# Se o resultado for maior que 15, imprima (ALTO) ao lado.
# Se o resultado for menor ou igual a 5, imprima (BAIXO).
# Caso contrário, não imprima nada extra.
# Saída esperada:

# text
# 1 x 1 = 1 (BAIXO)
# 1 x 2 = 2 (BAIXO)
# ...
# 4 x 4 = 16 (ALTO)
# ...

numeros = [1, 2, 3, 4, 5]


for numero in numeros:
    for i in numeros:
        multiplicacao = numero * i
        if multiplicacao >= 15:
            print(f'{numero} x {i} = {multiplicacao} (ALTO)')
        elif multiplicacao <= 5:
            print(f'{numero} x {i} = {multiplicacao} (BAIXO)')
        else: print(f'{numero} x {i} = {multiplicacao}')
    