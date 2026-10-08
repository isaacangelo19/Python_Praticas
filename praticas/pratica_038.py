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

valor_total_sudeste = 0
valor_total_nordeste = 0
valor_total_sul = 0

dicionario_vendas = {}

for id, venda in vendas.items():
    if venda['regiao'.strip().lower()] == 'Sudeste':
        valor_total_sudeste += venda['valor']
        dicionario_vendas['Sudeste'] = valor_total_sudeste
    if venda['regiao'.strip().lower()] == 'Nordeste':
        valor_total_nordeste += venda["valor"]
        dicionario_vendas['Nordeste'] = valor_total_nordeste
    if venda['regiao'.strip().lower()] == 'Sul':
        valor_total_sul += venda["valor"]
        dicionario_vendas['Sul'] = valor_total_sul
    if venda['regiao'.strip().lower()] == None:
        continue

print(dicionario_vendas)