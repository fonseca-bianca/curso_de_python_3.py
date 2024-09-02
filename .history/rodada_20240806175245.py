import random

class TimesQuadribol:
    def __init__(self, nome):
        self.nome = nome

class Partida:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def time_vencedor_partida(self):
        return random.choice([self.time1, self.time2])

class Rodada:
    def __init__(self, times):
        self.times = times
        self.rodada_atual = 1

    def sortear_adversarios_partida(self):
        random.shuffle(self.times)
        adversarios_partida = [(self.times[i], self.times[i+1]) for i in range(0, len(self.times), 2)]
        return adversarios_partida

    def exibir_adversarios_partida(self, adversarios_partida):
        print(f"Os times adversários na {self.rodada_atual}ª rodada são:")
        for i, (time1, time2) in enumerate(adversarios_partida, start=1):
            print(f"Partida {i}: {time1.nome} vs. {time2.nome}")

    def adversarios_rodada(self, adversarios_partida):
        times_vencedores = []
        for time1, time2 in adversarios_partida:
            partida = Partida(time1, time2)
            time_vencedor = partida.time_vencedor_partida()
            times_vencedores.append(time_vencedor)
        return times_vencedores

    def rodada_do_campeonato(self):
        while self.rodada_atual <= 3:
            if self.rodada_atual == 1:
                print(f"A {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = self.sortear_adversarios_partida()
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
                self.rodada_atual += 1

            elif self.rodada_atual == 2:
                print(f"\nA {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = self.sortear_adversarios_partida()
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
                self.rodada_atual += 1

            elif self.rodada_atual == 3:
                print(f"\nA {self.rodada_atual}ª rodada irá começar!")
                adversarios_partida = [(self.times[0], self.times[1])]
                self.exibir_adversarios_partida(adversarios_partida)
                self.times = self.adversarios_rodada(adversarios_partida)
                print(f"O time vencedor do campeonato é: {self.times[0].nome}")

# Exemplo de uso
times = [TimesQuadribol('Time A'), TimesQuadribol('Time B'), TimesQuadribol('Time C'), TimesQuadribol('Time D')]
rodada = Rodada(times)
rodada.rodada_do_campeonato()