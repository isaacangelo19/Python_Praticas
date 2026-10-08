vendas = {
    "2024-01-01": 1500,
    "2024-01-02": None,
    "2024-01-03": 2300,
    "2024-01-04": None,
    "2024-01-05": 1800
}

# 1. Limpeza de registros inválidos
# Você tem um dicionário de vendas onde alguns valores são None (dados faltantes). 
# Percorra e mostre apenas os registros válidos. Use continue para pular os inválidos.
for data, venda in vendas.items():
    if venda != None:
        print(f'Data {data} : valor {venda}')
    else: continue