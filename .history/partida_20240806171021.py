import random
import time

# cada partida terá 2 times se enfrentando
class Partida:
	# método construtor pra encapsulamento, polimorfismo e melhor reutilização código
	def __init__(self, time1, time2, valor_grito_time1, valor_grito_time2):
		self.time1 = time1
		self.time2 = time2
		self.valor_grito_time1 = valor_grito_time1
		self.valor_grito_time2 = valor_grito_time2
		self.placar = [50, 50]
		# cada time iniciará a partida com 50 pontos cada
		# colocado o placar com a pontuação inicial no método contrutor justamente pra garantir que
		# todos os Objetos (cada time) contidos em 'Partida' iniciem com o mesmo valor cada


# função desempatar o jogo quando encerrada a partida
def desempatar():
	count = 10
	while count >= 0:
		print(count)
		count -= 1
		time.sleep(1)
	if count <= 0:
		valor_grito_time1 = random.randrange(0, 10)
		valor_grito_time2 = random.randrange(0, 10)
		print(f"Valor grito time1: {valor_grito_time1}")
		print(f"Valor grito time2: {valor_grito_time2}")
	else:
		print("Não rodou")
	if valor_grito_time1 > valor_grito_time2:
		print("Time1 ganhou 3 pontos.")
	else:
		print("Time2 ganhou 3 pontos.")
desempatar()

# dicionário pros tipos de pontos e seus valores correspondentes
Tipo_de_Ponto = {"blot": 5, "plif": 1, "grusht": 3, "advrungh": -10}

