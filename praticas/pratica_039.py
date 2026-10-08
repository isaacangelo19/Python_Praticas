# 5. Soma de vendas por região
# Some o total de vendas por região. Ignore (com continue) registros sem região.

# python

# Objetivo: {"Sudeste": 2700, "Sul": 1750, "Nordeste": 1100}.

vendas = {
    "v1": {"regiao": "Sudeste", "valor": 1200},
    "v2": {"regiao": "Sul",     "valor": 800},
    "v3": {"regiao": "Sudeste", "valor": 1500},
    "v4": {"regiao": None,      "valor": 600},
    "v5": {"regiao": "Sul",     "valor": 950},
    "v6": {"regiao": "Nordeste","valor": 1100}
}

dicionario = {}

for id, venda in vendas.items():
    regiao = venda.get('regiao')
    valor = venda.get('valor', 0)
    if regiao == None:
        continue
    if regiao in dicionario:
        dicionario[regiao] += valor
    else:
        dicionario[regiao] = valor

print(dicionario)