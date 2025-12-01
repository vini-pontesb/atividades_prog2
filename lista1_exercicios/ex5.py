class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor
        return f"O depósito foi de R${valor} e o saldo atual é R${self._saldo}"

    def sacar(self, valor):
        if valor > self._saldo:
            return self._saldo
        self._saldo -= valor
        return self._saldo

    @property
    def saldoAtual(self):
        return self._saldo


conta = ContaBancaria("Vinicius Pontes Braga")
print(conta.saldoAtual)
conta.depositar(500)
print(conta.saldoAtual)
conta.sacar(200)
print(conta.saldoAtual)
conta.sacar(301)
print(conta.saldoAtual)