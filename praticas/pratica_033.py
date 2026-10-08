pessoas = {
    "Ana": {"idade": 25, "cidade": "São Paulo"},
    "Bruno": {"idade": 32, "cidade": "Rio de Janeiro"},
    "Carla": {"idade": 19, "cidade": "Belo Horizonte"},
    "Diego": {"idade": 41, "cidade": "Curitiba"}
}

# Crie um dicionário onde cada chave é o nome de uma pessoa 
# e o valor é outro dicionário com idade e cidade. 
# Percorra e mostre algo como:
# Ana tem 25 anos e mora em SP



for pessoa, caracteristicas in pessoas.items():
    print(f'{pessoa} tem {caracteristicas['idade']} e mora em {caracteristicas['cidade']}')
