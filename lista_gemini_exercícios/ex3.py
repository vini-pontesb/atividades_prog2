class Atleta:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Time:
    def __init__(self, nome_time):
        self.nome = nome_time
        self.lista_atletas = []

    def adicionar_atleta(self, atleta):
        self.lista_atletas.append(atleta)
        print(f">>> Atleta {atleta.nome} contratado pelo {self.nome}!")
    
    def transferir_atleta(self, atleta, outro_time):
        if atleta in self.lista_atletas:
            outro_time.lista_atletas.append(atleta)
            self.lista_atletas.remove(atleta)
            print(f"\n>>> Transferência realizada: {atleta.nome} foi do {self.nome} para o {outro_time.nome}.\n")
        else:
            print("O atleta não está nesse time")

    def listar_jogadores(self):
        print(f"\n---Jogadores do {self.nome}---\n")
        if not self.lista_atletas:
            print("O clube não possui jogadores")
            return
        for atleta in self.lista_atletas:
            print(f"{atleta.nome}, {atleta.idade} anos")

time1 = Time("Flamengo")
time2 = Time("Bangu")
atleta1 = Atleta("Emerson Royal", 26, "09867253865")
atleta2 = Atleta("Giorgian De Arrascarta", 31, "06387402743")
atleta3 = Atleta("Neymar Jr", 32, "12345678900")
time1.adicionar_atleta(atleta1)
time1.adicionar_atleta(atleta2)
time2.adicionar_atleta(atleta3)
time1.listar_jogadores()
time2.listar_jogadores()
time1.transferir_atleta(atleta1, time2)
time1.listar_jogadores()
time2.listar_jogadores()