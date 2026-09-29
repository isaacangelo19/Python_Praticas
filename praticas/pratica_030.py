palavra = "banana"
# ou peça ao usuário:
# palavra = input("Digite uma palavra: ")

# 3. Contador de caracteres
# Peça para o usuário digitar uma palavra. 
# Monte um dicionário onde cada letra seja uma chave e o valor seja quantas vezes ela aparece na palavra.
# No final, mostre o dicionário.
print('Digite uma palavra:')
palavra = input()

quantidade_caracteres = 0
for i in palavra:
    quantidade_caracteres += 1
print(f'A quantidade de caracteres da palavra {palavra} é {quantidade_caracteres}')