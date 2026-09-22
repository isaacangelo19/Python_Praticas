# Conte vogais em uma palavra
word = "Python"
vogais = 'aeiou   '

for i, item in enumerate(vogais.strip()):
    if i == 4:
        continue
    else: 
        print(f'{i} : {item}')
    



print(enumerate(word))