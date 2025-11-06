#as variáveis têm diferentes escopos (visibilidade)
x= 10
#variavel global
def funcao():
    #Variavel local
    y = 5
    print(f" Dentro da função - x:{x}, y: {y}")
y= funcao()
funcao() #Saída: Dentro da função - x: 10, y: 5
# A variavel y não está disponível
print(f"Fora da função - x: {x}")
print(f"y: {y}")
 # Erro: nome y não está definido