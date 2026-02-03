from abc import ABC, abstractmethod
import random
class ErroPagamento(Exception):
    pass

class SaldoInsuficienteError(ErroPagamento):
    nome = 'erro_saldo_insuficiente'
    pass

class GatewayForaDoArError(ErroPagamento):
    nome = 'erro_fora_do_ar'
    pass

class CartaoBloqueadoError(ErroPagamento):
    nome = 'erro_cartao_bloqueado'
    pass


class GatewayPagamento(ABC):

    @abstractmethod
    def autorizar_pagamento(self, valor):
        pass

    @abstractmethod
    def capturar_valor(self, id):
        pass

    @abstractmethod
    def estornar(self, id):
        pass

    def gerar_log_transacao(self):
        print('Salvando arquivo .txt')


class PayPalGateway(GatewayPagamento):
    def __init__(self):
        self.pagamentos = []

    def autorizar_pagamento(self, valor):
        self.pagamentos.append(valor)
        excecoes = [SaldoInsuficienteError().nome, GatewayForaDoArError().nome, CartaoBloqueadoError().nome]
        nome_excecao = random.choice(excecoes)
        if nome_excecao is SaldoInsuficienteError().nome:
            excecao = SaldoInsuficienteError()
            raise excecao("SALDO INSUFICIENTE")
        elif nome_excecao is GatewayForaDoArError().nome:
            excecao = GatewayForaDoArError()
            raise excecao("GATEWAY PORA DO AR")
        elif nome_excecao is CartaoBloqueadoError().nome:
            excecao = CartaoBloqueadoError()
            raise excecao("CARTÃO BLOQUEADO")

    def capturar_valor(self, id):
        print(
            f'O valor do pagamento (Paypal) de id {id} é de R${self.pagamentos[id-1]}.')

    def estornar(self, id):
        print(
            f'O pagamento (Paypal) de id {id} (R${self.pagamentos[id-1]}) será estornado.')
        self.pagamentos.pop(id-1)
        print(f'O pagamento (Paypal) de id {id} foi estornado.')

    def get_pagamentos(self):
        return self.pagamentos


class StripeGateway(GatewayPagamento):
    def __init__(self):
        self.pagamentos = []

    def autorizar_pagamento(self, valor):
        self.pagamentos.append(valor)
        print(f'Pagamento (Stripe) no valor de R${valor} autorizado.')

    def capturar_valor(self, id):
        print(
            f'O valor do pagamento (Stripe) de id {id} é de R${self.pagamentos[id-1]}.')

    def estornar(self, id):
        print(
            f'O pagamento (Stripe) de id {id} (R${self.pagamentos[id-1]}) será estornado.')
        self.pagamentos.pop(id-1)
        print(f'O pagamento (Stripe) de id {id} foi estornado.')

    def get_pagamentos(self):
        return self.pagamentos


class ProcessadorDePedidos():
    def __init__(self):
        self.contrato = []

    def inserir_contrato(self, contrato):
        self.contrato.append(contrato)

    def get_contratos(self):
        return self.contrato

try:

    paypal = PayPalGateway()
    v1 = float(input('Insira o valor do pagamento (PyPal)\nR$: '))
    paypal.autorizar_pagamento(v1)
    print(f'Pagamentos: {paypal.get_pagamentos()}')
    id1 = 1
    paypal.capturar_valor(id1)
    paypal.estornar(id1)
    print(f'Pagamentos: {paypal.get_pagamentos()}')

    stripe = StripeGateway()
    v2 = float(input('Insira o valor do pagamento (Stripe)\nR$: '))
    stripe.autorizar_pagamento(v2)
    print(f'Pagamentos: {stripe.get_pagamentos()}')
    id2 = 1
    stripe.capturar_valor(id2)
    stripe.estornar(id2)
    print(f'Pagamentos: {stripe.get_pagamentos()}')

    processador = ProcessadorDePedidos()
    processador.inserir_contrato(paypal)
    processador.inserir_contrato(stripe)
    print(processador.get_contratos())

except SaldoInsuficienteError as e:
    print(f'ERRO: {e}')
except GatewayForaDoArError as e:
    print(f'ERRO: {e}')
except CartaoBloqueadoError as e:
    print(f'ERRO: {e}')
