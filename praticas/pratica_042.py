# 6. Média de três notas
# Crie media que recebe três notas e retorna a média.

def media_notas(nota1 = float, nota2 = float, nota3 = float):
    """Calcula a média de notas """
    media = (nota1 + nota2 + nota3) / 3
    print(f'A média é {media:.2f}')

media_notas(8,8,10)
