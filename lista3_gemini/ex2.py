class Processador:
    def __init__(self):
        self.memoria = False

    def memoria_inserida(self):
        self.memoria = True

    def memoria_retirada(self):
        self.memoria = False

    def verificar_memoria(self):
        if self.memoria == True:
            print("Computador ligado com sucesso!")
        else:
            print("Erro ao ligar o computador, sem memória ram.")


class MemoriaRam:
    pass


class PlacaMae:

    def inicializar_processador(self, processador):
        processador.verificar_memoria()


class Computador():
    def __init__(self):
        self.processador = Processador()
        self.placa_mae = PlacaMae()
        self.memoria_ram = []

    def inserir_memoria_ram(self, memoria):
        self.memoria_ram.append(memoria)
        self.processador.memoria_inserida()
        print('Memoria ram inserida')

    def remover_memoria_ram(self, memoria):
        self.memoria_ram.remove(memoria)
        self.processador.memoria_retirada()
        print('Memoria ram retirada')

    def ligar(self):
        self.placa_mae.inicializar_processador(self.processador)


m1 = MemoriaRam()
pc = Computador()
pc.ligar()
pc.inserir_memoria_ram(m1)
pc.ligar()
pc.remover_memoria_ram(m1)
pc.ligar()
