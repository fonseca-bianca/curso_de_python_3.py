import random
import time 

class Partida:

	def __init__(self, time1, time2, valor_grito):
		self.time1 = time1
		self.time2 = time2
		self.valor_grito = valor_grito


		# cada time iniciará a partida com 50 pontos cada
		# colocado o placar com a pontuação inicial no método contrutor justamente pra garantir que
		# todos os Objetos (cada time) contidos em 'Partida' iniciem com o mesmo valor cada
		self.placar = [50, 50]

	# função para desempatar o jogo quando encerrada a partida

def desempatar():
	valor_grito = 0
	count = 15


	while count >= 0:
		print(count)
		count -= 1
		time.sleep(1)

	if count <= 0:
		valor_grito = random.randrange(0, 10)
		print(f"Valor grito {valor_grito}")
	else:
		print("Não rodou")