#condição o programa verificará
# se a nota é menor que 5(reprovado). Se não,
#verifica se a nota é menor que 7 (rec)
#Caso nenhuma dessas condições seja verdadeira, imprime "Aprovado"

aluno = input("Insira o nome: ")
nota = int(input("Insira sua nota: "))

if nota >=0 and nota <5:
    print("Aluno está reprovado")
elif nota >=0 and nota <7:
    print("Aluno está de Recuperação ")
elif nota <= 10 and nota >=7:
    print("Aluno está Aprovado") 
else :
    print("Desculpe, sua nota é invalida")