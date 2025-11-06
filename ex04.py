'''Construa um programa para fazer uma pequena entrevista com
os alunos de uma turma. Na entrevista, são informados o sexo e
a idade de cada aluno. considere que o usuário não sabe quantos
alunos existem na turma. O programa deve exibir a quantidade de
homens acima de 18 anos e a quantidade de mulheres de 
qualquer idade. Para encerrar o programa, o usuário deve informar
uma idade negativa.'''

# Inicializando os contadores
homens_acima_18 = 0
total_mulheres = 0

print("=== Entrevista com os alunos ===")
print("Digite uma idade negativa para encerrar.\n")

while True:
    try:
        idade = int(input("Informe a idade do aluno: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido para a idade.")
        continue

    # Condição de parada
    if idade < 0:
        print("\nEntrevista encerrada.")
        break

    sexo = input("Informe o sexo (M/F): ").strip().upper()

    # Validação do sexo
    while sexo not in ('M', 'F'):
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
        sexo = input("Informe o sexo (M/F): ").strip().upper()

    # Lógica de contagem
    if sexo == 'M' and idade > 18:
        homens_acima_18 += 1
    elif sexo == 'F':
        total_mulheres += 1

# Exibindo os resultados
print("\n=== Resultados da Entrevista ===")
print(f"Quantidade de homens com mais de 18 anos: {homens_acima_18}")
print(f"Quantidade de mulheres (qualquer idade): {total_mulheres}")
