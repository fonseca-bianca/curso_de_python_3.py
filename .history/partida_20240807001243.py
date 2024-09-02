import time as t
import random
from quadribol_teams import Quadribol_Teams  

class Partida:
    duracao_partida = 180

    def __init__(self, team1, team2, valor_grito_team1, valor_grito_team2):
        self.team1 = team1
        self.team2 = team2
        self.valor_grito_team1 = valor_grito_team1
        self.valor_grito_team2 = valor_grito_team2
        self.placar = [50, 50]
        self.inicio = t.time()

    def encontrar_team_por_nome(self, nome):
        if self.team1.nome == nome:
            return self.team1
        elif self.team2.nome == nome:
            return self.team2
        print(f"Time '{nome}' não encontrado.")
        return None

    def atualizar_placar(self, index_team, ponto):
        if 0 <= index_team < len(self.placar):
            self.placar[index_team] += ponto

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
        print(f"Placar: {self.team1.nome}: {self.placar[0]} vs. {self.team2.nome}: {self.placar[1]}")

def desempatar(team1, team2):
    count = 10
    while count >= 0:
        print(count)
        count -= 1
        t.sleep(1)
    if count < 0:
        valor_grito_team1 = random.randrange(0, 10)
        valor_grito_team2 = random.randrange(0, 10)
        print(f"Valor grito team1: {valor_grito_team1}")
        print(f"Valor grito team2: {valor_grito_team2}")
        if valor_grito_team1 > valor_grito_team2:
            print("Team1 ganhou 3 pontos (grusht).")
        else:
            print("Team2 ganhou 3 pontos (grusht).")