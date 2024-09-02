import random
from partida import Partida


# rodada: irá fazer o sorteio dos times adversários, controlar o resultado das partidas e
# fazer o gerenciamento da pontuação dos times ao final de cada partida
# aqui está a lógica principal do sistema, pois há o controle de cada time e o resultado final com o campeão

class TimesQuadribol:
    def __init__(self, nome):
        self.nome = nome

class Partida:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def time_vencedor_partida(self):
       ### return random.choice([self.time1, self.time2])

class Rodada:
    def __init__(self, times):
        self.times = times
        self.rodada_atual = 1

    def sortear_adversarios_partida(self):
        random.shuffle(self.times)
        adversarios_partida = [(self.times[i], self.times[i+1]) for i in range(0, len(self.times), 2)]
        return adversarios_partida