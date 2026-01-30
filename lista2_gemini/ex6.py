class Motor:
    def ligar(self):
        print("vruuuumm")

class Carro:
    def __init__(self):
        self._motor = Motor()

    def ligar_carro(self):
        self._motor.ligar()

carro = Carro()
carro.ligar_carro()