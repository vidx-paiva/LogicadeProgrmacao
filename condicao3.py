#Elabore um programa que receba o nome do dia da semana e imprima:
#"Fim de semana" se for sábado ou somingo;
#"Início da semana" se for segunda-feira;
#"Dia útil" para os outros dias

dia = input("Dgite o dia: ").strip().lower()

if dia == "sábado" or dia == "sabado" or dia =="domingo":
    print("Fim de semana!")
elif dia == "segunda-feira" or dia == "segunda":
    print("Início da semana.")
elif dia == "terça-feira" or dia == "terça" or dia == "quarta-feira" or dia == "quarta" or dia == "quinta-feira" or dia == "quinta":
    print("Dia útil")
else:
    print("Dia invalido")