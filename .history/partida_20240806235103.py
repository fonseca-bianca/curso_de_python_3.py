import time as t
import random
from quadribol_times import Quadribol_Times  # Certifique-se de que o arquivo está no mesmo diretório

class Partida:
    duracao_partida = 180

    def __init__(self, time1, time2, valor_grito_time1, valor_grito_time2):
        self.time1 = time1
        self.time2 = time2
        self.valor_grito_time1 = valor_grito_time1
        self.valor_grito_time2 = valor_grito_time2
        self.placar = [50, 50]
        self.inicio = t.time()

    def encontrar_time_por_nome(self, nome):
        if self.time1.nome == nome:
            return self.time1
        elif self.time2.nome == nome:
            return self.time2
        print(f"Time '{nome}' não encontrado.")
        return None

    def atualizar_placar(self, index_time, ponto):
        if 0 <= index_time < len(self.placar):
            self.placar[index_time] += ponto

    def pontuacao(self):
        tempo_decorrido = t.time() - self.inicio
        tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))

        if tempo_restante <= 0:
            print("A partida terminou.")
            return

        evento = {
            "blot": 5,
            "plif": 1,
            "advrungh": -10,
            "expecto_patronum": 1
        }

        evento_ocorrido = random.choice(list(evento.keys()))
        ponto = evento[evento_ocorrido]

        if evento_ocorrido == "blot":
            print("O time ganhou 5 pontos (blot).")
            self.atualizar_placar(0, ponto)

        elif evento_ocorrido == "plif":
            print("O time ganhou 1 ponto (plif).")
            self.atualizar_placar(0, ponto)

        elif evento_ocorrido == "advrungh":
            print("O time perdeu 10 pontos (advrungh).")
            self.atualizar_placar(0, ponto)

        elif evento_ocorrido == "expecto_patronum":
            print("O time ganhou 1 ponto (expecto patronum).")
            self.atualizar_placar(0, ponto)

    def mostrar_placar(self):
        print(f"Placar: {self.time1.nome}: {self.placar[0]} vs. {self.time2.nome}: {self.placar[1]}")