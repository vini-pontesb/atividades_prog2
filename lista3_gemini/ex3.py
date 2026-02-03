from abc import ABC, abstractmethod 
import random

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
        print(f'Pagamento (Paypal) no valor de R${valor} autorizado.')

    def capturar_valor(self, id):
        print(f'O valor do pagamento (Paypal) de id {id} é de R${self.pagamentos[id-1]}.')

    def estornar(self, id):
        print(f'O pagamento (Paypal) de id {id} (R${self.pagamentos[id-1]}) será estornado.')
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
        print(f'O valor do pagamento (Stripe) de id {id} é de R${self.pagamentos[id-1]}.')

    def estornar(self, id):
        print(f'O pagamento (Stripe) de id {id} (R${self.pagamentos[id-1]}) será estornado.')
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