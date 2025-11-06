saldo_bancario = int(input("Qual seu saldo? "))


#Recebeu um depósito
deposito = int(input("Qual seu depósito? "))
saldo_total = saldo_bancario + deposito 

#Pagou uma conta
conta = int(input("Qual valor da conta? "))
saldo_total = saldo_bancario - conta + deposito

print(saldo_total) 