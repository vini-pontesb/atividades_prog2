class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, outro_ponto):
        ponto2 = outro_ponto
        x1 = self.x
        y1 = self.y
        x2 = ponto2.x
        y2 = ponto2.y
        dist = (((x2-x1)**2) + ((y2-y1)**2))**0.5
        return dist


primeiro_ponto = Ponto(10, 5)
segundo_ponto = Ponto(2, 7)
mensagem = primeiro_ponto.distancia(segundo_ponto)
print(mensagem)
