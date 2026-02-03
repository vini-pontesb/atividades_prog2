class ValorInvalidoError(Exception):
    pass
class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError(f'O valor {valor} é invalido, ele deve positivo')
        self.saldo += valor
        print( f'O valor de R${valor} foi depositado.\nSaldo atual: R${self.saldo}')

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f'O valor a ser sacado deve ser menor que o saldo.\nSaldo atual: R${self.saldo}')
        self.saldo -= valor
        print( f'O valor de R${valor} foi sacado.\nSaldo atual: R${self.saldo}')

verificacao = True
while verificacao == True:
    try:
        conta = ContaBancaria("Vinicius")
        v1 = float(input('Insira o valor a ser depositado: '))
        conta.depositar(v1)
        v2 = float(input('Insira o valor a ser sacado: '))
        conta.sacar(v2)
        v3 = float(input('Insira o valor a ser sacado: '))
        conta.sacar(v3)
        continuacao = int(input('Insira PARAR para terminar o uso: '))
        if continuacao == 'PARAR':
            verificacao = False
    except ValorInvalidoError  as e:
        print(f'ERRO: {e}')
        continuacao = int(input('1 - Continuar\n2 - Parar\n: '))
        if continuacao == 2:
            verificacao = False
    except SaldoInsuficienteError  as e:
        print(f'ERRO: {e}')
        continuacao = int(input('1 - Continuar\n2 - Parar\n: '))
        if continuacao == 2:
            verificacao = False