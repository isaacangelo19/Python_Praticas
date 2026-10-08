# 4. Contagem de categorias
# Você tem uma lista de produtos com categoria. 
# Monte um dicionário contando quantos produtos existem por categoria. (Clássico em pipelines.)

# python

# ]
# Objetivo: gerar algo como {"roupa": 3, "eletrônico": 3, "cozinha": 1}.
produtos = [
    {"nome": "camisa",  "categoria": "roupa"},
    {"nome": "celular", "categoria": "eletrônico"},
    {"nome": "calça",   "categoria": "roupa"},
    {"nome": "fone",    "categoria": "eletrônico"},
    {"nome": "meia",    "categoria": "roupa"},
    {"nome": "tv",      "categoria": "eletrônico"},
    {"nome": "panela",  "categoria": "cozinha"}]

dicionario = {}
contador_roupa = 0
contador_eletronico = 0
contador_cozinha = 0
for produto in produtos:
    if produto['categoria'] == 'roupa':
        contador_roupa += 1
        dicionario['roupa'] = contador_roupa
    if produto['categoria'] == 'eletrônico':
          contador_eletronico += 1
          dicionario['eletrônico'] = contador_eletronico
    if produto['categoria'] == 'cozinha':
        contador_cozinha += 1
        dicionario['cozinha'] = contador_cozinha

print(dicionario)

