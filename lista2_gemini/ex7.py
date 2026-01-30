from abc import ABC, abstractmethod

class FormaPagamento(ABC):

    @abstractmethod
    def processar(self, valor):
        self.valor = valor
        return self.valor

try:
    pag = FormaPagamento()
except TypeError as e:
    print(f"ERRO: {e}")