class ContaBancaria:
    def __init__ (self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado.")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def ver_saldo(self):
        return