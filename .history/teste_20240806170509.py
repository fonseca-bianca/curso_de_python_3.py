import random

from time import Time
from partida import Partida

# rodada: irá fazer o sorteio dos times adversários, controlar o resultado das partidas e
# fazer o gerenciamento da pontuação dos times ao final de cada partida
# aqui está a lógica principal do sistema, pois há o controle de cada time e o resultado final com o campeão


class Time:
	def __init__(self, nome):
		self.nome = nome

class Partida:
	def __init__(self, time1, time2):
		self.time1 = time1
		self.time2 = time2

	def time_vencedor_partida(self): #jogar
		# o time que obtiver maior pontuação ao final da partida será o time vencedor
		time_vencedor_partida = random.choice([self.time1], [self.time2]) #time vencedor entre a dupla que está disputando a partida
		return time_vencedor_partida

class Rodada:
	def __init__(self, times):
		self.times = times
		self.rodada_atual = 1


	def sortear_adversarios_partida(self, times): #sortear_duplas
		random.shuffle(times)
		adversarios_partida = [(times[i], times[i+1])
							   for i in range(0, len(self.times), 2)]
		return adversarios_partida

	def exibir_adversarios_partida(self, adversarios_partida): #exibir_partidas #duplas
		print(f"Os times adversários na {self.rodada_atual}ª são:")
		for i, (time1, time2) in enumerate(adversarios_partida, start=1):
			print(f"Partida {i}: {time1.nome} vs. {time2.nome}")


	def adversarios_rodada(self, adversarios_partida): #jogar_rodada
		times_vencedores = []
		for time1, time2 in adversarios_partida:
			partida = Partida(time1, time2)
			times_vencedores = partida.time_vencedor_partida()
			times_vencedores.append(times_vencedores)
		return times_vencedores

	def rodada_do_campeonato(self):
		while self.rodada_atual <= 3:
			if self.rodada_atual == 1:
				print(f"A {self.rodada_atual}ª rodada irá começar!")
				adversarios_partida = self.sortear_adversarios_partida(self.times)
				self.exibir_adversarios_partida(adversarios_partida)
				self.times = self.adversarios_rodada(adversarios_partida)
				self.rodada_atual += 1
			elif self.rodada_atual == 2:
				print(f"\nA {self.rodada_atual}ª rodada irá começar!")
				adversarios_partida = self.sortear_adversarios_partida(self.times)
				self.exibir_adversarios_partida(adversarios_partida)
				self.times = self.adversarios_rodada(adversarios_partida)
				self.rodada_atual += 1
			elif self.rodada_atual == 3:
				print(f"\nA {self.rodada_atual}ª rodada irá começar!")
				adversarios_partida = [(self.times[0], self.times[1])]
				self.exibir_adversarios_partida(adversarios_partida)
				self.times = self.adversarios_rodada(adversarios_partida)
				print(f"O time vencedor do campeonato é: {self.times[0].nome}")

def inicio_campeonato():
	nome_do_time = [time.nome for time in inserir_dados()]
	campeonato_quadribol = Rodada(nome_do_time)
	campeonato_quadribol.rodada_do_campeonato()

if __name__ == '__main__':
	inicio_campeonato()