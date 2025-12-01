class Escritor:
    def __init__(self, nome):
        self.nome = nome
    def escrever (self, pen):
        caneta = Caneta(pen)
        print(f"O escritor {self.nome} está a escrever com a caneta {caneta.marca}")

class Caneta:
    def __init__(self, marca):
        self.marca = marca

escritor1 = Escritor("Vinicius")
escritor1.escrever("Bic")