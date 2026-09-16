# Crie uma lista com 6 números. 
# Use um for para criar uma nova lista onde cada elemento é o dobro do original. 
# Imprima a nova lista.

lista = [30,20,50,10,44]

lista_dobro = []

for i in lista:
    dobro = i * 2
    lista_dobro.append(dobro)
print(lista_dobro)