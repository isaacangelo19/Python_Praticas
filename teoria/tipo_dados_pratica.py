menu = "menu".title()
preco_nordestina = 65.3300
preco_frango = 60.510
preco_calabresa = 62.545454

print(menu.center(30, '-'))
print("pizza nordestina ".title().ljust(40, '.'),"\t" ,round(preco_nordestina, 1))
print("pizza frango ".title().ljust(40, '.'), '\t', round(preco_frango, 1))
print("pizza calabresa ".title().ljust(40, '.'), '\t', 'R$', round(preco_calabresa, 2))

print('\n\n\n\n')

### quantificador de caracteres
print('quantificador de caracteres'.title().center(60, '.'))
nome = str(input('Digite seu nome: '))
todoscaracteres = len(nome)
excluindoespacos = nome.strip()
print('O número de caracteres totais incluindo os espaços é: ', todoscaracteres)
print('O número de caracteres totais sem incluir os espaços é: ', len(excluindoespacos))
print(nome.strip())