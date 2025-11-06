#Crie um programa em Python que funcione como uma calculadora básica, usando funções para cada operação matemática (soma, subtração, multiplicação e divisão).
#O programa deve exibir um menu com as opções de operação para o usuário escolher. Após a seleção, o programa solicitará dois números e, em seguida, chamará a função correspondente para calcular o resultado.
#O resultado deve ser exibido ao usuário.
#O programa deve continuar executando até que o usuário escolha sair.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def menu():
    print("\nCalculadora Básica")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao == "5":
            print("Saindo...")
            break
        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, digite valores numéricos válidos.")
                continue

            if opcao == "1":
                resultado = soma(num1, num2)
            elif opcao == "2":
                resultado = subtracao(num1, num2)
            elif opcao == "3":
                resultado = multiplicacao(num1, num2)
            elif opcao == "4":
                resultado = divisao(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
