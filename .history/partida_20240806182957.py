import random
import time

import random
import time

# Cada partida terá 2 times se enfrentando
class Partida:
    def __init__(self, time1, time2, valor_grito_time1, valor_grito_time2):
        self.time1 = time1
        self.time2 = time2
        self.valor_grito_time1 = valor_grito_time1
        self.valor_grito_time2 = valor_grito_time2
        self.placar = [50, 50]
        self.inicio = time.time()  # Marca o início da partida

    def atualizar_placar(self, time_index, pontos):
        if 0 <= time_index < 2:
            self.placar[time_index] += pontos

    def pontuacao(self):
        tempo_decorrido = time.time() - self.inicio
        tempo_restante = max(0, 180 - int(tempo_decorrido))  # Tempo restante em segundos

        if tempo_restante <= 0:
            print("A partida terminou.")
            return

        evento = random.choice(['blot', 'plif', 'advrungh', 'expecto patronum'])

        if evento == 'blot':
            print("O time ganhou 5 pontos (blot).")
            self.atualizar_placar(0, 5)  # Supondo que seja o time1, ajuste conforme necessário
        elif evento == 'plif':
            print("O time ganhou 1 ponto (plif).")
            self.atualizar_placar(0, 1)  # Supondo que seja o time1, ajuste conforme necessário
        elif evento == 'advrungh':
            print("O time ou a torcida cometeu irregularidade. O time perdeu 10 pontos (advrungh).")
            self.atualizar_placar(0, -10)  # Supondo que seja o time1, ajuste conforme necessário
        elif evento == 'expecto patronum':
            if tempo_restante <= 30:
                print("O time ganhou 1 ponto (expecto patronum) por acertar a bola na trave adversária.")
                self.atualizar_placar(0, 1)  # Supondo que seja o time1, ajuste conforme necessário

    def mostrar_placar(self):
        print(f"Placar - {self.time1}: {self.placar[0]}, {self.time2}: {self.placar[1]}")

# Exemplo de uso
time1 = "Time A"
time2 = "Time B"
partida = Partida(time1, time2, 10, 15)

# Simula a partida por alguns segundos
time.sleep(10)  # Aguarda 10 segundos
partida.pontuacao()  # Aplica a pontuação

partida.mostrar_placar()
