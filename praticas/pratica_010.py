word = "Python"
vogais = 'aeiou   '


for w, v in zip(word, vogais):
    print(f'{w} : {v}')



print(list(zip(word,vogais)))

lista = list(zip(word,vogais))

print(lista[0])