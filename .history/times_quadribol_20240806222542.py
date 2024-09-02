import random

class TimeQuadribol:
    # ... (mesma definição da classe)

def criar_times():
    # ... (mesma função para criar os times)

def sortear_times(times, num_times_sortear):
    times_sorteados = []
    for _ in range(num_times_sortear):
        time_sorteado = random.choice(times)
        times_sorteados.append(time_sorteado)
        times.remove(time_sorteado)
    return times_sorteados

def realizar_rodada(times_sorteados):
    print("RODADA NUMERO 1")
    for i in range(0, len(times_sorteados), 2):
        time1 = times_sorteados[i]
        time2 = times_sorteados[i + 1]
        print(f"A primeira partida é {time1.nome} VS {time2.nome}")

# Criar os times
times = criar_times()

# Sortear 8 times para a primeira rodada
num_times_por_rodada = 8
times_rodada1 = sortear_times(times, num_times_por_rodada)

# Realizar a rodada
realizar_rodada(times_rodada1)