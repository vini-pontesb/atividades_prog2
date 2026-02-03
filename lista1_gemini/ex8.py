from abc import ABC, abstractmethod


class GerenciadorPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class Cartao(GerenciadorPagamento):
    def __init__(self):
        self.tipo = "Cartão"

    def pagar(self, valor):
        print(f"Pagamento no valor de R${valor} no cartão")

    def tipo(self):
        return f"O tipo do pagamento é: {self.tipo}"


class Pix(GerenciadorPagamento):
    def __init__(self):
        self.tipo = "Pix"

    def pagar(self, valor):
        print(f"Pagamento no valor de R${valor} no pix")

    def tipo(self):
        return f"O tipo do pagamento é: {self.tipo}"

cartao1 = Cartao()
print(cartao1.tipo)
cartao1.pagar(100)
pix1 = Pix()
print(pix1.tipo)
pix1.pagar(200)
