class Jogador:
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time 
        self.jogadores = []
    
    def adicionar_jogadores(self, jogador):
        self.jogadores.append(jogador)

verificacao = True
team = Time(input("Insira um time: "))
while verificacao == True:
    player = Jogador(input("Insira o jogador que será a nova contratação: ")) 
    team.adicionar_jogadores(player.nome_jogador)
    pergunta = int(input("Siga as instruções:\n1 - Continuar contratando\n2 - Parar de contratar\n: "))
    if pergunta == 2:
        verificacao = False
        
print(f"Jogadores contratados do time {team.nome_time}: {team.jogadores}")