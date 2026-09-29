dicionario = {
    'chave 1' : 1,
    'chave 2' : 2,
    'chave 3' : 3
}

for x in dicionario.keys():
    print(f'chave : {x}')

print('')

for y in dicionario.values():
    print(f'valor : {y}')

print('')

for x, y in dicionario.items():
    print(f'Chave: {x} | Valor : {y}')


dicionario = [{
    'chave 1' : 1,
    'chave 2' : 2,
    'chave 3' : 3
}]
print('')
print('Colocando dentro de uma lista'.center(50, '#'))

dicionario = [{
    'chave 1' : 1,
    'chave 2' : 2,
    'chave 3' : 3
}]

for x in dicionario:
    for chave in x.keys():
        print(chave)
    for valor in x.values():
        print(valor)
    for chave, valor in x.items():
        print(f'Chave: {chave} | Valor : {valor}')

print('')
print('Colocando values dentro de uma lista'.center(50, '#'))

dicionario = [{
    'chave 1' : [1,2,3],
    'chave 2' : [4,5],
    'chave 3' : [5]
}]

for chave_valor in dicionario:
    print(chave_valor)
    for chave in chave_valor.keys():
        print(chave)
    for valor in chave_valor.values():
        print(valor)
    for chave, valor in chave_valor.items():
        soma = sum(valor)
        #print(f'{chave}: {soma}')
        for i in valor:
            if i % 2 == 0:
                print(f'{chave}: {i} par')
            else : print(f'{chave}: {i} ímpar')