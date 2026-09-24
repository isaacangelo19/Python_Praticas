
# O que fazer:

# Percorra cada registro.
# Valide: nome não pode ser vazio, email precisa ter @, idade entre 0 e 120.
# Se passar, limpe: remova espaços do nome, coloque em title case, email em minúsculo.
# Separe em duas listas: aprovados e rejeitados.
# No final, imprima quantos foram aprovados, quantos rejeitados e os registros limpos.

registros_brutos = [
    {"id": 1, "nome": "  joão  ", "email": "JOAO@EMAIL.COM", "idade": 22},
    {"id": 2, "nome": "", "email": "maria@email.com", "idade": 20},
    {"id": 3, "nome": "Carlos", "email": "carlos_email_invalido", "idade": -5},
    {"id": 4, "nome": "  Ana  ", "email": "ANA@EMAIL.COM", "idade": 25},
    {"id": 5, "nome": "Pedro", "email": "", "idade": 0}
]
aprovados = 0
rejeitados = 0
tem_erro = False

for registro in registros_brutos:
    tem_erro = False
    if registro['nome'] == '':
        tem_erro = True
        print(f'O id {registro['id']} está com erro no nome')
    if '@' not in registro['email']:
        tem_erro = True
        print(f'O id {registro['id']} está com erro no email')
    if registro['idade'] > 120 or registro["idade"] < 0:
        tem_erro = True
        print(f'O id {registro['id']} está com erro na idade')
    if tem_erro == True:
        rejeitados += 1
    else: aprovados += 1
print("")
print(f' Aprovados: {aprovados} | Rejeitados: {rejeitados} ')




