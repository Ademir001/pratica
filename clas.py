class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def saldo(self):
        return self.saldo
    
    def deposito(self,valor):
        if valor > 0:
            self.__saldo +=valor
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

conta = Conta("Ana", 1000)
conta.deposito(500)
print(conta.saldo())  
conta.sacar(2000)               