lista1 = [1,3,4,5,6]
lista2 = [3,1,4,5,6]

print(lista1 == lista2)

dicionario1 = {
    1 : 'chave 1',
    2 : 'chave 2'
}

dicionario2 = {
    2 : 'chave 2',
    1 : 'chave 1'
}

print(dicionario1 == dicionario2)



livro_001 = {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "genero": "Romance",
        "disponivel": True,
        "emprestimos": 12}

for k, v in livro_001.items():
    print(f"Chave : {k}  valor : {v}")




biblioteca = {
    "livro_001": {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "genero": "Romance",
        "disponivel": True,
        "emprestimos": 12
    },
    "livro_002": {
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "ano": 1937,
        "genero": "Fantasia",
        "disponivel": False,
        "emprestimos": 25
    },
    "livro_003": {
        "titulo": "Sapiens",
        "autor": "Yuval Noah Harari",
        "ano": 2011,
        "genero": "História",
        "disponivel": True,
        "emprestimos": 8
    },
    "livro_004": {
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "genero": "Distopia",
        "disponivel": True,
        "emprestimos": 30
    },
    "livro_005": {
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1943,
        "genero": "Infantil",
        "disponivel": False,
        "emprestimos": 18
    }
}

print("")

print(biblioteca["livro_002"]['titulo'])


print("")
