transacoes = {
    "TX001": {"valor": 2500, "status": "aprovada"},
    "TX002": {"valor": 300,  "status": "aprovada"},
    "TX003": {"valor": 5000, "status": "negada"},
    "TX004": {"valor": 1200, "status": "aprovada"},
    "TX005": {"valor": 800,  "status": "pendente"}
}

# 2. Filtrando transações suspeitas
# Você tem transações com valor e status. 
# Mostre apenas as aprovadas e com valor acima de 1000. Use if combinado.

for id, transacao in transacoes.items():
    if transacao['status'.lower().strip()] == 'aprovada' and transacao['valor'.lower().strip()] > 1000:
        print(f'Transação : {id} {transacao["status"]}')