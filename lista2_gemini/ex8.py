from abc import ABC, abstractmethod


class FormaPagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class Pix(FormaPagamento):
    def processar(self, valor):
        return f'Processando PIX no valor de R${valor}'

class CartaoCredito(FormaPagamento):
    def processar(self, valor):
        return f'Validando cartão no valor de R${valor}'

p = Pix()
print(p.processar(20.50))
c = CartaoCredito()
print(c.processar(20.45))