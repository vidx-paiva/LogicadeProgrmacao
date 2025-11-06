idade = int(input("Insira sua idade: "))

if idade >=0 and idade <=13:
    print("Criança")
elif idade >=0 and idade <=20:
    print("Adolescente")
elif idade >=0 and idade <=60:
    print("Adulto")
elif idade >=0 and idade >= 60:
    print("Idoso")
else:
    print("Recem nascido ou morto?")