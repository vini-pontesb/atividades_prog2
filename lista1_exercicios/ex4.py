class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def calcular_area(self):
        area = self.altura * self.largura
        return f"A área é {area}"


ret = Retangulo(20, 30)
print(ret.calcular_area)