import random

class Time:
    def __init__(self, nome):
        self.nome = nome

class Partida:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
    
    def jogar(self):
        vencedor = random.choice([self.time1, self.time2])
        return vencedor

def sortear_duplas(times):
    random.shuffle(times)
    duplas = [(times[i], times[i+1]) for i in range(0, len(times), 2)]
    return duplas

def exibir_partidas(rodada, duplas):
    print(f"Os times que vão se enfrentar na {rodada}ª rodada são:")
    for i, (time1, time2) in enumerate(duplas, start=1):
        print(f"Partida {i}: {time1.nome} vs. {time2.nome}")

def jogar_rodada(duplas):
    vencedores = []
    for time1, time2 in duplas:
        partida = Partida(time1, time2)
        vencedor = partida.jogar()
        vencedores.append(vencedor)
    return vencedores

def rodada_campeonato(times):
    rodada_atual = 1
    while rodada_atual <= 3:
        if rodada_atual == 1:
            print(f"\nA {rodada_atual}ª rodada irá começar!")
            duplas = sortear_duplas(times)
            exibir_partidas(rodada_atual, duplas)
            times = jogar_rodada(duplas)
        elif rodada_atual == 2:
            print(f"\nA {rodada_atual}ª rodada irá começar!")
            duplas = sortear_duplas(times)
            exibir_partidas(rodada_atual, duplas)
            times = jogar_rodada(duplas)
        elif rodada_atual == 3:
            print(f"\nA {rodada_atual}ª rodada irá começar!")
            duplas = [(times[0], times[1])]
            exibir_partidas(rodada_atual, duplas)
            times = jogar_rodada(duplas)
            print(f"O time vencedor do campeonato é: {times[0].nome}")
        rodada_atual += 1

def iniciar_campeonato():
    times = [Time(f"Time {i+1}") for i in range(8)]
    rodada_campeonato(times)

if __name__ == "__main__":
    iniciar_campeonato()