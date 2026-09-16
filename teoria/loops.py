# Objetivo: Criar um programa que imprime os números de 1 a 10 usando while.

# O que fazer:

# Crie uma variável numero = 1.
# Use um while para imprimir o valor de numero.
# Dentro do loop, incremente o numero em 1.
# O loop deve parar quando numero for maior que 10.

# numero = 1
# while numero <= 20:
#     numero += 1
#     if numero > 10:
#         print("Programa parado pois chegamos no número 10")
#         break
#     print(numero)


# Objetivo: Pedir números ao usuário e somar tudo, até ele digitar 0.

# O que fazer:

# Crie uma variável soma = 0.
# Use while True: (loop infinito controlado).
# Peça um número ao usuário com input().
# Converta para int.
# Se o número for 0, use break para sair.
# Se não for 0, some na variável soma.
# No final (depois do loop), imprima a soma total.

# soma = 0 

# while True:
#     numero = int(input("Digite um número, caso queira terminar a soma dos números digite 0: "))
#     print(f"Você digitou : {numero}")
#     soma += numero
#     if numero == 0:
#         break
# print(f"A soma total dos números adicionado é: {soma}")


# Objetivo: Pedir uma senha até o usuário acertar.

# O que fazer:

# Defina uma senha correta (ex: senha_correta = "1234").
# Use while True:.
# Peça a senha ao usuário.
# Se a senha estiver correta, imprima "Acesso permitido" e use break.
# Se estiver errada, imprima "Senha incorreta. Tente novamente."

# senhacorreta = 'flamengo1234'

# while True:
#     senhausuario = input('Digite a senha: ')
#     if senhausuario == senhacorreta:
#         print("Acertou a senha")
#         break
#     print("Digite a senha novamente, senha incorreta")

# Objetivo: Criar um programa que percorre números de 1 a 20, mas com regras específicas de pulo e parada.

# O que fazer:

# Crie uma variável numero = 0.
# Use while True: (loop infinito controlado).
# Dentro do loop, incremente numero em 1 no início.
# Regra 1 (break): Se numero for maior que 20, imprima "Limite atingido. Encerrando..." e use break.
# Regra 2 (continue): Se numero for par, use continue (não imprime nada).
# Regra 3 (continue): Se numero for múltiplo de 3, use continue (não imprime nada).
# Regra 4: Se não caiu em nenhuma das regras acima, imprima o número.

# numero = 0
# while True:
#     numero += 1
#     if numero > 20:
#         break
#     if numero % 2 == 0:
#         continue
#     if numero % 3 == 0:
#         continue
#     print(numero)

# Objetivo: Simular um caixa eletrônico que só aceita valores múltiplos de 10, com saldo inicial limitado e opção de sair.

# Regras:

# O saldo inicial é R$ 100,00.
# O programa deve rodar em loop até o usuário digitar 0 para sair.
# O menu deve ser:
# 1 - Sacar
# 2 - Ver saldo
# 0 - Sair
# Regra 1 (continue): Se o usuário digitar uma opção inválida (diferente de 0, 1 ou 2), imprima "Opção inválida." e use continue para voltar ao menu.
# Regra 2 (continue): Se o usuário escolher "Sacar" e digitar um valor que não seja múltiplo de 10, imprima "O valor deve ser múltiplo de 10." e use continue.
# Regra 3 (continue): Se o usuário tentar sacar mais do que o saldo disponível, imprima "Saldo insuficiente." e use continue.
# Regra 4 (break): Se o usuário digitar 0, imprima "Saindo..." e use break.
# Se o saque for válido, subtraia do saldo e imprima "Saque realizado. Saldo atual: R$ X".


    

# for x in range(100):
#     if x % 2 != 0:
#         continue
#     if x % 2 == 0:
#         print(x)

# for x in range(100):
#     if x % 10 != 0:
#         continue
#     print(x)

for x in range(0, 100, 5):
    print(x)
