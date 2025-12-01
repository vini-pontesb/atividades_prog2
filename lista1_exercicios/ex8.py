class Animal:
    especie = "mamífero"
    
    def __init__(self, nome):
        self.nome = nome
    
    @property
    def detalhes(self):
        print(f"O nome do animal é {self.nome} e sua espécie é {Animal.especie}")

bicho = Animal("cachorro")
bicho.detalhes
