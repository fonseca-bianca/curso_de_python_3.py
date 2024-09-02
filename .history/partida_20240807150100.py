import time as t
import random
from quadribol_teams import inserir_dados, sorteia_partidas

class Partida:
	duracao_partida = 180

	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2
		self.placar = [50, 50]
		self.inicio = t.time()
		self.valor_grito_team1 = 0
		self.valor_grito_team2 = 0

	def encontrar_time_por_nome(self, nome):
		if self.team1.nome == nome:
			return self.team1
		elif self.team2.nome == nome:
			return self.team2
		print(f"Time '{nome}' não encontrado.")
		return None

	def atualizar_placar(self, index_team, tipo_de_ponto):
		if 0 <= index_team < len(self.placar):
			self.placar[index_team] += tipo_de_ponto

	def pontuacao(self):
		tempo_decorrido = t.time() - self.inicio
		tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))

		if tempo_restante <= 0:
			print("A partida terminou.")
			return

		tipo_de_ponto = {
			"blot": 5,
			"plif": 1,
			"advrungh": -10,
			"expecto_patronum": 1
		}

		tipo_de_ponto_escolhido = random.choice(list(tipo_de_ponto.keys()))

		if tipo_de_ponto_escolhido == "blot":
			print("O time ganhou 5 pontos (blot).")
			self.atualizar_placar(0, tipo_de_ponto[tipo_de_ponto_escolhido])

		elif tipo_de_ponto_escolhido == "plif":
			print("O time ganhou 1 ponto (plif).")
			self.atualizar_placar(0, tipo_de_ponto[tipo_de_ponto_escolhido])

		elif tipo_de_ponto_escolhido == "advrungh":
			print("O time perdeu 10 pontos (advrungh).")
			self.atualizar_placar(0, tipo_de_ponto[tipo_de_ponto_escolhido])

		elif tipo_de_ponto_escolhido == "expecto_patronum":
			print("O time ganhou 1 ponto (expecto patronum).")
			self.atualizar_placar(0, tipo_de_ponto[tipo_de_ponto_escolhido])

	def mostrar_placar(self):
		print(f"Placar: {self.team1.nome}: {self.placar[0]} vs. {self.team2.nome}: {self.placar[1]}")

	def desempatar(self):
		count = 10
		while count >= 0:
			print(count)
			count -= 1
			t.sleep(1)

		if count <= 0:
			self.valor_grito_team1 = random.randrange(0, 10)
			self.valor_grito_team2 = random.randrange(0, 10)
			print(f"Valor grito time1: {self.valor_grito_team1}")
			print(f"Valor grito time2: {self.valor_grito_team2}")

			if self.valor_grito_team1 > self.valor_grito_team2:
				print("Time1 ganhou 3 pontos (grusht).")
				self.atualizar_placar(0, 3)
			else:
				print("Time2 ganhou 3 pontos (grusht).")
				self.atualizar_placar(1, 3)

# Exemplo de uso
if __name__ == "__main__":
	teams = inserir_dados()
	partidas = sorteia_partidas(teams)

	# Primeira rodada
	for i, (team1, team2) in enumerate(partidas):
		partida = Partida(team1, team2)
		print(f"Partida {i+1}: {team1.nome} vs. {team2.nome}")
		partida.pontuacao()
		partida.mostrar_placar()
		if partida.placar[0] == partida.placar[1]:
			partida.desempatar()
			partida.mostrar_placar()

