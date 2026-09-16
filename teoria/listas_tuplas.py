usuarios = ['isaac', 'sara', 'gab']
print('Isaac'.lower() in usuarios)

print(usuarios[0])
print(usuarios[-1])


print(usuarios.index('GAB   '.lower().rstrip()))

print('')

usuarios.append('tom')



usuarios += ['penelope', 'bela']


usuarios.insert(0, 'plata')

print(usuarios[2:3])
print('')
usuarios[2:3] += [1,2,3]
print('')
lista = ['ISAAC   '.rstrip().lower(), 'gab']
print(lista.index('isaac        '.rstrip().lower()))


lista = [1,2,3,4]
lista.extend([6,7,8,9,9])

lista.insert(0, [-1,0])
lista[:2] += [-1,0]
print(lista)


lista.remove(1)
print(lista)

lista.pop(10)
print(lista)

del lista[0]
print(lista)

print(usuarios)

lista.clear()
print(lista)

usuarios.remove(1)
usuarios.remove(2)
usuarios.remove(3)
print(usuarios)

usuarios.sort()
print(usuarios)

usuarios.sort(key=str.lower)
print(usuarios)

usuarios.reverse()
print(usuarios)

usuarios.sort(reverse=False)
print(usuarios)

numeros = [1,5,2,7,10,64,69,67,30]

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

numeros.sort(key=int, reverse=True)
print(numeros)


nums = [1,4,5,7,7,7,7]
nums.remove(7)
print(nums)
nums.remove(7)
print(nums)


numeros = [2,1,-5,-80,20]
numeros.sort(reverse=True)
print(numeros)

numeros.reverse()
print(numeros)

listass = [4,2,'isaac', 'sara']
listass.sort(key=str, reverse=True)
print(listass)


# Fila do Banco
# Crie uma lista vazia chamada fila.
# Adicione 3 clientes comuns que vão chegando ao final da fila.
# Chegou um cliente idoso: insira ele diretamente na primeira posição (índice 0).
# Mostre na tela quem é o primeiro da fila e quem é o último da fila usando índices.
# Chame o primeiro cliente para o atendimento, removendo-o da fila e guardando o nome dele em uma variável para exibir a mensagem "Atendendo cliente X".
# Um cliente do meio da fila desistiu de esperar pelo nome: encontre e remova esse cliente específico da lista.
print('')
print('')
print('')
print('')
print('')

lista = []
lista.append('cliente1')
lista.append('cliente2')
lista.append('cliente3')

print(lista)

lista.insert(0, 'cliente_idoso1')
print(lista)

print('')
print(f'O primeiro cliente da fila é o {lista[0]} e o último da fila é {lista[3]}')

lista.pop(0)

atendendo_cliente = 'cliente_idoso1'

print(f'Estamos atendendo o cliente {atendendo_cliente}')

lista.pop(1)

print(f"Esses são os próximos da fila {lista}")

print('')
print('')
print('')
print('')

lista01 = [3,55,-4,-3.5]
print(lista01)

lista02 = lista01.copy()
print(lista02)

lista03 = lista01[:]
lista03.sort(reverse=True)
print(lista03)

lista04 = list([3,5,7,-2])
print(lista04)

tupla01 = tuple(('flamengo', 'arsenal'))
print(type(tupla01))
print(tupla01)

tupla01 = list(tupla01)
print(type(tupla01))
tupla01.append('isaac')
tupla01.sort(key=str, reverse= False)
print(tupla01)
tupla01 = tuple((tupla01))
print(type(tupla01))
print(tupla01)

print(tupla01.count('sara'))

tupla02 = (3,2,2,1,4,56,6,6) 
print(tupla02)

tupla03 = tuple([2,3,4,5,6,6,7])
print(tupla03)

tupla05 = (2,3,5)
print(tupla05)