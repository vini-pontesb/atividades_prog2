from datetime import datetime

class LogMixin:
    def log(self, mensagem):
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return f"[{data_hora}] {mensagem}."

class ConexaoBanco(LogMixin):
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def conectar(self):
        msg = super().log(f"Você se conectou ao banco {self.nome} - {self.numero}")
        print(msg)
    
    def desconectar(self):
        msg = super().log(f"Você se desconectou ao banco {self.nome} - {self.numero}")
        print(msg)

nome_banco = input("Insira o nome do banco: ")
numero_banco = input("Insira o numero do banco: ")
b1 = ConexaoBanco(nome_banco, numero_banco)
pergunta = int(input("Digite 1 para conecatar e 2 para desconectar\n--> "))
while pergunta != 1 and pergunta != 2:
    pergunta = int(input("Você digitou errado, tente novamente.\nDigite 1 para conecatar e 2 para desconectar\n--> "))
if pergunta == 1:
    b1.conectar()
else:
    b1.desconectar()