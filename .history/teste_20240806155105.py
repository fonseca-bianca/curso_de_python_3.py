def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
        self.nome = nome
        self.grito_de_guerra = grito_de_guerra
        self.ano_de_fundacao = ano_de_fundacao

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

def gerar_partidas(times, rodada_atual):
    vencedores = []
    if rodada_atual == 1:
        random.shuffle(times)
        for i in range(0, len(times), 2):
            partida = Partida(times[i], times[i+1])
            vencedor = partida.jogar()
            print(f"O time vencedor da partida {i//2 + 1} é: {vencedor.nome}")
            vencedores.append(vencedor)
    elif rodada_atual == 2:
        random.shuffle(times)
        for i in range(0, len(times), 2):
            partida = Partida(times[i], times[i+1])
            vencedor = partida.jogar()
            print(f"O time vencedor da partida {i//2 + 1} é: {vencedor.nome}")
            vencedores.append(vencedor)
    elif rodada_atual == 3:
        partida = Partida(times[0], times[1])
        vencedor = partida.jogar()
        print(f"O time vencedor da partida final é: {vencedor.nome}")
        vencedores.append(vencedor)
    return vencedores

def rodada_campeonato(times):
    rodada_atual = 1
    while rodada_atual <= 3:
        print(f"A {rodada_atual}ª rodada irá começar!")
        times = gerar_partidas(times, rodada_atual)
        rodada_atual += 1

def iniciar_campeonato():
    times = [Time(f"Time {i+1}") for i in range(8)]
    rodada_campeonato(times)

if __name__ == "__main__":
    iniciar_campeonato()