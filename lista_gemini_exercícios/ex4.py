class Predio:
    def __init__(self):
        self.apartamentos = []

    def inserir_apartamento(self, numero, andar):
        apartamento = Apartamento(numero, andar)
        self.apartamentos.append(apartamento)

    def listar_apartamento(self):
        print("-"*5, "Listagem de todos os apartamentos", "-"*5)
        for ap in self.apartamentos:
            print(f"          Andar: {ap.andar} | Número: {ap.numero}")


class Apartamento:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar


predio1 = Predio()
predio1.inserir_apartamento(702, 7)
predio1.inserir_apartamento(703, 7)
predio1.inserir_apartamento(604, 6)
predio1.listar_apartamento()
