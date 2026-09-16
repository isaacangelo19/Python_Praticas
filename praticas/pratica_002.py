# Crie uma lista com 8 números. 
# Use um for para contar quantos números são maiores que 10. Imprima o resultado.

lista = list(range(4, 50, 8))

numeros_maior_10 = 0

for i in lista:
    if i > 10 :
        numeros_maior_10 += 1
        print(f"O número {i} é maior que 10 e foi adicionado")

print(f"A quantidade de números maiores que 10 na lista é : {numeros_maior_10}")
