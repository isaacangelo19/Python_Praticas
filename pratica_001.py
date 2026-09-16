# Crie uma lista com 5 números inteiros. 
# Use um for para percorrer a lista e imprimir a soma total

inteiros = list(range(6))
print(inteiros)

soma_total = 0

for i in inteiros:
    soma_total += i
print(f'A soma total é: {soma_total}')