'''1. Crie um programa no qual o usuário informe um número
inteiro positivo N e armazene-0 em uma variável. Em seguida,
o usuário deve digitar N números. Ao Fim, o programa deve
imprimir a média aritmética dos N números digitados. '''

# Solicita ao usuário um número inteiro positivo
N = int(input("Digite a quantidade de números que você deseja inserir (N): "))

# Verifica se N é positivo
if N <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    soma = 0  # Variável para armazenar a soma dos números

    # Loop para ler os N números
    for i in range(N):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma += numero  # Soma os números

    # Calcula a média aritmética
    media = soma / N

    # Exibe a média
    print(f"A média aritmética dos {N} números é: {media:.2f}")
