class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    
class MixinNadador:
    def atacar(self):
        print('Mergulha com o inimigo')

class MixinVoador:
    def atacar(self):
        print('Voa por cima')

class MixinMagico:
    def lancar_magia(self):
        print('Lança fogo')

class Paladino(Personagem, MixinNadador, MixinMagico):
    pass

class Dragao(Personagem, MixinVoador,  MixinMagico, MixinNadador):
    def atacar(self):
        return super().atacar()

dragao = Dragao("Dagrão", 2)
print(dragao.nome)
print(dragao.nivel)
print(Dragao.mro())
