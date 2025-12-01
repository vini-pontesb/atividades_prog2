class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

    def sacar(self, valor):
        if valor > self._saldo:
            return self._saldo
        self._saldo -= valor
        return self._saldo
    
    def __str__(self):
        return f"O saldo do titular {self.titular} é R${self._saldo}"

conta = ContaBancaria("Vinicius Pontes Braga")
print(conta)
conta.depositar(500)
print(conta)
conta.sacar(200)
print(conta)
conta.sacar(301)
print(conta)