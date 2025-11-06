'''Crie um programa que recebe 5 numeros digitados e, ao fim,
exibe quantos números são pares. '''


# Inicializa o contador de números pares
quantidade_pares = 0

# Loop para receber 5 números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    # Verifica se o número é par
    if numero % 2 == 0:
        quantidade_pares += 1

# Exibe o resultado
print(f"Você digitou {quantidade_pares} número(s) par(es).")
