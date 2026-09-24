# Regras de validação:

# O cliente não pode ser vazio.
# O valor tem que ser maior que 0.
# O status só pode ser "pago" ou "pendente" (se for "cancelado", o pedido é rejeitado).

pedidos = [
    {"id": 1, "cliente": "João", "valor": 150.00, "status": "pago"},
    {"id": 2, "cliente": "", "valor": 200.00, "status": "pago"},
    {"id": 3, "cliente": "Carlos", "valor": -50.00, "status": "pendente"},
    {"id": 4, "cliente": "Ana", "valor": 300.00, "status": "cancelado"},
    {"id": 5, "cliente": "Pedro", "valor": 0.00, "status": "pago"},
    {"id": 6, "cliente": "Maria", "valor": 450.00, "status": "pago"}
]
pedidos_certo = 0
pedidos_errado = 0
valor_total = 0
for pedido in pedidos:
    erro = False
    if pedido['cliente'] == '':
        erro = True
        print(f'O {pedido['id']} está com nome vazio')
    if pedido['valor'] < 0:
        erro = True
        print(f'O {pedido['id']} está com valor negativo')
    if pedido['status'] not in ['pago'.strip().lower(), 'pendente'.strip().lower()]:
        erro = True
        print(f'O {pedido['id']} está com erro de status')
    if erro == True:
        pedidos_errado += 1
    else: pedidos_certo += 1
    if erro == False:
        valor_total += pedido['valor']

print(f'Pedidos corretos: {pedidos_certo} | Pedidos com erro: {pedidos_errado} | valor_total: {valor_total}')
    