print("*** Operação de divisão** ")

while True:
    n1 = int(input("informe o primeiro número: "))
    n2 = int(input("informe o segundo número: "))
    if n2 == 0:
        print("Divisor não pode ser 0. \n Programa será encerrado... ")
        break
    print(f"{n1} / {n2} = {(n1/n2):.2f}")