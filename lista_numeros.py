#implemente uma função que receba uma lista de números e 
#retorne o maior valor dessa lista.
def maior_valor(lista):
    if not lista:
        return "Lista VAZIA!"
    
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [int(x) for x in entrada.split()]

print(f"O maior número da lista é {maior_valor(lista_numeros)}")