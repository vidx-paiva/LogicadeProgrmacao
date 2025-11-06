#Crie uma função chamada soma que receba 
#dois números como parâmetros e retorne a 
#soma deles. Depois, peça para o usuário digitar dois 
#números, utilize a função para somá-los e imprima o 
#resultado

def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    return num1 + num2
    

resultado = soma()
print("A soma dos dois números é:", resultado)
