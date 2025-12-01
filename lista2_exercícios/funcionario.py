class Funcionario:
    def __init__(self, salario, cargo):
        self._salario = salario
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        salario_atual = self.salario
        if novo_salario < salario_atual:
            print("Seu novo salário é mais baixo que o atual")
            self._salario = novo_salario
            return
        self._salario = novo_salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self._cargo = novo_cargo


funcionario1 = Funcionario(2500, "Assistente 1")
print(funcionario1.salario)
print(funcionario1.cargo)
funcionario1.cargo = "Estagio"
funcionario1.salario = 1500
print(funcionario1.cargo)
print(funcionario1.salario)
funcionario1.cargo = "Assistente 2"
funcionario1.salario = 3500
print(funcionario1.cargo)
print(funcionario1.salario)
