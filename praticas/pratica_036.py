logs = {
    1: {"nivel": "INFO",     "msg": "sistema iniciado"},
    2: {"nivel": "INFO",     "msg": "conexão ok"},
    3: {"nivel": "WARNING",  "msg": "latência alta"},
    4: {"nivel": "CRITICAL", "msg": "falha no banco"},
    5: {"nivel": "INFO",     "msg": "tentando reconectar"}
}

# 3. Parar ao encontrar erro crítico
# Percorra um dicionário de logs. Se encontrar um log com nível "CRITICAL", 
# mostre a mensagem e pare o processamento com break.

for id, log in logs.items():
    if log['nivel'].strip().upper() == 'CRITICAL'.strip().upper():
        print(f'id {id} CRITICAL')
        break
    else: print(f'id {id} {log['msg']}')