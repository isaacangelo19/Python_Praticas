# 5. Área do retângulo (boa nomeação)
# Crie calcular_area_retangulo que recebe base e altura e retorna a área. 
# Note como o nome comunica a intenção.

def area_retangulo(base = float(), altura = float()):
    """Essa função serve para calcular a área """
    area = base * altura
    print(area)

area_retangulo(base= 20, altura= 40)