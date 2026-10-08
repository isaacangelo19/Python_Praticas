## Definindo funções
def soma(a,b,c):
    print(a + b + c)

def saudacao(nome, profissao):
    """Demonstração do nome 
        e profissão"""
    print(f'Olá {nome.title()}. Sua profissão é {profissao.title()}')


### Arguments positional
#### No caso da saudação já inferimos que será passsado primeiro o nome e depois a profissão

print(saudacao('engenheiro de dados', 'isaac'))

### Keyword arguments
#### Nesse caso ao chamar a função já passamos o nome no parâmetro

print(saudacao(nome= 'isaac', profissao='Engenheiro de Dados'))
print(saudacao(profissao='engenheiro de dados', nome= 'isaac'))

### values default
#### Nesse caso podemos já trazer um valor padrão dentro da função
def pet(nome, animal = 'Cachorro'):
    print(f'Seu animal é {animal.title()} e o nome {nome}')

pet(nome = 'gab')


### print e return
#### O return retorna um valor para o código e o print serve apenas para mostrar na tela

def soma(a = float, b = float):
    return a + b 
print('')
print(soma(5,5) + 2)

def soma_print(a = float, b = float):
    print(a + b)
print('')

print(soma_print(5,5) + 2)