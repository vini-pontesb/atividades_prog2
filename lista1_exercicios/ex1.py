class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


person = Pessoa("Vinicius Pontes", 21)
print(person.nome)
print(person.idade)
