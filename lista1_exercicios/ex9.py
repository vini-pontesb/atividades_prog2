class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self._notas = []

    def adicionar_nota(self, nota):
        self._notas.append(nota)

    @property
    def calcular_media(self):
        soma = sum(self._notas)
        quantidade = len(self._notas)
        media = soma/quantidade
        return media


estudante1 = Estudante("Vinicius", 12345)
estudante1.adicionar_nota(10)
estudante1.adicionar_nota(8)
print(estudante1.calcular_media)
