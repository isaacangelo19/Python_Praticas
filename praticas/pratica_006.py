# Crie uma lista com 10 palavras. 
# Use um for para contar quantas palavras têm mais de 5 letras. Imprima o total.

times = ['flamengo', 'platense', 'ldu', 'fluminense', 'estudiantes', 'corinthians', 'palmeiras', 'del valle']
maior_5_letras = 0
menor_5_letras = 0
for i in times:
    if len(i.strip()) > 5:
        maior_5_letras += 1
    else: menor_5_letras += 1

print(f"times com mais de 5 letras: {maior_5_letras}")
print(f"times com menos de 5 letras: {menor_5_letras}")