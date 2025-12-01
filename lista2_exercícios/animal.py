class Animal:
    def emitir_som(self):
        print("Som genérico")


class Cachorro(Animal):
    def emitir_som(self):
        print("AuAu")


class Gato(Animal):
    def emitir_som(self):
        print("Miau")


theo = Cachorro()
theo.emitir_som()
garfield = Gato()
garfield.emitir_som()
