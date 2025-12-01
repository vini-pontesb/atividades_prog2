import math


class FormaGeometrica:
    def __init__(self, nome_forma):
        self.nome_forma = nome_forma

    def area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
        super().__init__("Quadrado")

    def area(self):
        area = self.lado**2
        print(area)


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        super().__init__("Circulo")

    def area(self):
        area = math.pi*self.raio**2
        print(round(area, 2))


quadrado1 = Quadrado(5)
quadrado1.area()
circulo1 = Circulo(5)
circulo1.area()
print(quadrado1.nome_forma)
