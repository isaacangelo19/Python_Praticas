dicionario = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3'
}

dicionario2 = dict(chave1= 'valor1', chave2= 'valor2')

print(dicionario)
print(dicionario2)
print(type(dicionario))
print(type(dicionario2))

### acessando items

print(dicionario['chave1'])
print(dicionario.get('chave2'))

### listando todas as chaves e valores
print(dicionario.keys())
print(dicionario.values())

### listando todas as chaves e valores por meio de tupla
print(dicionario.items())

### mudar valores no dicionario
dicionario['chave1'] = 'valor01'
dicionario['chave2'] = 'valor02'
dicionario['chave3'] = 'valor03'

print(dicionario.items())

dicionario.update({'chave 4': 'valor4', 'chave 5' : 'valor 5'})
print(dicionario.items())


### removendo valores de dicionario

print(dicionario.pop('chave 5'))
print(dicionario)

dicionario.popitem()
print(dicionario)

del dicionario['chave3']
print(dicionario)

print(dicionario2)
dicionario2.clear()
print(dicionario2)