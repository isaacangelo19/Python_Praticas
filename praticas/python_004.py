import sys 
import random
# print('')


# banda = input('Escolha uma banda: \n 1 para Oasis \n 2 para Green Day \n 3 para CBJ \n sua resposta: ')
# int_banda = int(banda)

# if int_banda < 1 or int_banda > 3:
#     sys.exit('Voce deve escolher um número de 1 a 3')

# escolha_computador = random.choice(range(1,4))

# int_escolha_computador = int(escolha_computador)

# print('')
# print('Sua escolha foi : ', int_banda)
# print('Escolha do computador : ', int_escolha_computador)


# if int_banda == 1 and int_escolha_computador == 1:
#     print('Escolheram a mesma banda')
# elif int_banda > int_escolha_computador:
#     print('Voce ganhou do computador')
# else: print("O computador ganhou")



# import random

# numero_input = input('Digite um número: ')
# computador = random.choice(range(1,50))
# numero = int(numero_input)

# print('')
# print(f'O número que você escolheu foi : {numero}')
# print(f'O número que o computador escolheu foi : {computador}')
# print('')

# if numero > computador:
# 	print('Parabens, voce ganhou')
# elif numero < computador:
# 	print('O computador ganhou')
# else: print('Voces escolheram o mesmo numero')


print('MENU'.capitalize().center(20, '-'))
print('')
print('pizza'.capitalize().ljust(20, '.'), 'R$', round(float('60.0203435'), 4))
print('hamburguer'.capitalize().ljust(20, '.'),'R$', round(float('15.0302735'), 4))

escolha = input('Escolha o que deseja: \n 1 para pizza \n 2 para hamburguer: ')
int_escolha = int(escolha)
computador = random.choice(range(1,2))

print(f'    Sua escolha foi {int_escolha}'.rstrip().ljust(20).lstrip())
print(f'A escolha do computador foi {computador}    '.lstrip().rjust(20))