# Percorra a lista frutas e imprima cada fruta com seu número de posição (começando em 1).
# As frutas "uva" e "abacaxi" devem ser ignoradas.

# Saída esperada:

# text
# 1 - maçã
# 2 - banana
# 3 - laranja
# 5 - manga
# 7 - melancia

frutas = ["maçã", "banana", "laranja", "uva  ", "manga", "abacaxi ", "melancia"]

for indice, fruta in enumerate(frutas, start= 1):
    if fruta.lower().strip() == 'uva' or fruta.lower().strip() == 'abacaxi':
        continue
    else: print(f'{indice} - {fruta}')