class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @property
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos"

person = Pessoa("Vinicius Pontes", 21)
print(person.apresentar)