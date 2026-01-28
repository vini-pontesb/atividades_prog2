class Telefone:
    def fazer_chamada(self):
        print("Piririm")

class Camera:
    def tirar_foto(self):
        print("Tic")

class Smartphone(Telefone, Camera):
    pass

telefone = Smartphone()
telefone.fazer_chamada()
telefone.tirar_foto()