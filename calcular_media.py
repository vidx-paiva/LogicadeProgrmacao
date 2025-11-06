# Crie uma função chamada calcular_media(nota_a, nota_b)
# que recebe as duas notas, calcula a média ponderada e
# retorna o resultado. A função principal leria as
# entradas e chamaria calcular_media

def calcular_media(nota_a, nota_b):
    # Peso 0,4 para nota_a e 0,6 para nota_b
    media = (nota_a * 0.4) + (nota_b * 0.6)
    return media

# Função principal para leitura das notas
def main():
    nota_a = float(input("Digite a primeira nota: "))
    nota_b = float(input("Digite a segunda nota: "))
    resultado = calcular_media(nota_a, nota_b)
    print(f"A média ponderada é: {resultado:.2f}")

# Chamando a função principal
if __name__ == "__main__":
    main()
