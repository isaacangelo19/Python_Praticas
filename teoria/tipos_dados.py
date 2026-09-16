saudacao = """"
Olá, 
    como você está?

    Estou realizando um teste neste programa

"""

print(saudacao)

teste_espacos = ''''
Vamos
    Flamengo
        ser
            penta
'''

print(teste_espacos)

barras = 'hi, i\'m isaac e i\'m excited\t\t\twith this opportunity \n i want know more' 
print(barras)

prox_linha = '          oi\ncomo voce \nvai?\n                    '

print(prox_linha)

print(prox_linha.upper())
print(prox_linha.title())
print(prox_linha.replace('vai', 'está'))

print(len(prox_linha))

print(len(prox_linha.strip()))
print('quantidade de caracteres sem espaço na esquerda : \t', len(prox_linha.lstrip()) )
print('quantidade de caracteres sem espaço na direita : \t', len(prox_linha.rstrip())) 

print("")

menu = 'menu'.upper()
print(menu.center(20, "-" ))
print("Café".ljust(20, '.') + "" + "4 R$".rjust(10))
print("Refrigerante".ljust(20, '.') + "6 R$".rjust(10) + "\n")

print('Café'.ljust(20, '-'))
print('Refrigerante'.rjust(20, '-'))

time = 'flamengo'
print(time.upper().startswith('F'))
print(time.upper().endswith('O'))
print("\n\n")

### TRABALHANDO COM INTEIROS
melhor_preco = int(30)
print(type(melhor_preco))
preco = 100
print(isinstance(preco, int))