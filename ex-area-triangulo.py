# Faça uma função que recebe base e altura e retorna a área do triângulo usa
# área = (base x altura) / 2

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Exemplo de uso:
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

print(f"A área do triângulo é: {area_triangulo(base, altura)}")
