import random
from time import Time  
from partida import Partida

class Partida:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def time_vencedor_partida(self):
        # O time que for escolhido aleatoriamente entre os dois
        time_vencedor_partida = random.choice([self.time1, self.time2])
        return time_vencedor_partida

class Rodada:
    def __init__(self, times):
        self.times = times
        self.rodada_atual = 1

    def sortear_adversarios_partida(self, times):
        random.shuffle(times)
        adversarios_partida = [(times[i], times[i+1]) for i in range(0, len(times), 2)]
        return adversarios_partida

    def exibir_adversarios_partida(self, adversarios_partida):
        print(f"Os times adversários na {self.rodada_atual}ª rodada são:")
        for i, (time1, time2) in enumerate(adversarios_partida, start=1):
            print(f"Partida {i}: {time1.nome} vs. {time2.nome}")

    def adversarios_rodada(self, adversarios_partida):
        times_vencedores = []
        for time1, time2 in adversarios_partida:
            partida = Partida(time1, time2)
            vencedor = partida.time_vencedor_partida()
            times_vencedores.append(vencedor)
        return times_vencedores

    def rodada_do_campeonato(self):
        while self.rodada_atual <= 3:
            if self.rodada_atual == 1:
                print(f"A {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = self.sortear_adversarios_partida(self.times)
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
            elif self.rodada_atual == 2:
                print(f"\nA {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = self.sortear_adversarios_partida(self.times)
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
            elif self.rodada_atual == 3:
                print(f"\nA {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = [(self.times[0], self.times[1])]
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
                print(f"O time vencedor do campeonato é: {self.times[0].nome}")

            self.rodada_atual += 1

def inserir_dados():
    # Exemplo de dados, substitua com o código para realmente obter os dados dos times
    return [Time(f"Time {i+1}") for i in range(8)]

def inicio_campeonato():
    nomes_times = [time.nome for time in inserir_dados()]
    campeonato_quadribol = Rodada(nomes_times)
    campeonato_quadribol.rodada_do_campeonato()

if __name__ == '__main__':
    inicio_campeonato()