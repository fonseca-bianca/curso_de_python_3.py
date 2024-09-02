import random

# cada partida terá 2 times se enfrentando
class Partida:
	def __init__(self, time1, time2):
		self.time1 = time1
		self.time2 = time2
		# cada time iniciará a partida com 50 pontos cada
		# colocado o placar com a pontuação inicial no método contrutor justamente pra garantir que
		# todos os Objetos (cada time) contidos em 'Partida' iniciem com o mesmo valor cada
		self.placar = [50, 50]

#REFAZEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEER
# função que sorteia os times adversários de uma partida
def sorteio_de_times(self):
	# sorteio aleatório (random) que retorna True e False (espécie de Cara ou Koroa)
	# valor retornado True: bloco dentro do if será executado. Times self.time1 e self.time2 serão trocados de lugar
	# valor retornado False: bloco dentro do if NÃO será executado. Times self.time1 e self.time2 NÃO serão trocados de lugar
	if random.choice([True, False]):
		self.time1, self.time2 = self.time2, self.time1

# função para simular uma partida com pontuações variadas entre os times
def simulacao_de_partida(self):
	# função 'randint' irá gerar pontuação variada (diferente da função 'choice' que mantém a pontuação)
	self.placar[0] += random.randint([50, 100])
	self.placar[1] += random.randint([50, 120])


# dicionário pros tipos de pontos e seus valores correspondentes
Tipo_de_Ponto = {"blot": 5, "plif": 1, "grusht": 3, "advrungh": -10}


# função que valida o ponto se ele estiver dentro do dicionário 'Tipo_de_Ponto'
# caso o ponto não esteja na lista, aparecerá uma mensagem de erro pro usuário
def validacao_do_ponto(self, time, tipo_do_ponto):
	if tipo_do_ponto not in Tipo_de_Ponto:
		raise ValueError("O tipo de ponto não é válido.")

	# chave: 'tipo_do_ponto' e seu valor é armazenado na variável 'pontuacao'
	pontuacao = Tipo_de_Ponto[tipo_do_ponto]
	indice_time = self.time1 == time
	# self.time1: verifica se o time que fez o ponto é o time1 da partida
	# indice_time: o resultado acima irá verificar se o ponto: foi feito pelo time1 (True), se não, (False)
	# o resultado da verificação True/False é armazenado na variável 'indice_time'

	self.placar[indice_time] += pontuacao
	# self.placar: aqui contém a lista com os times e seus respectivos pontos
	# time1 = índice 0, time2 = índice 1 da lita
	# += pontuacao: o valor total dos pontos de cada partida é somado ao elemento da lista de times. Placar do jogo é atualizado


# função FEATURE EXTRA: implementei essa funcionalidade extra ao jogo
# cada time terá a chance de ganhar 10 pontos se acertar a jogada bônus
# caso o jogador não acerte, o time não será penalizado e nem perderá pontos
def pontuacao_bonus(self, time):
	# se time acertar a jogada (50% chance acerto), o time irá ganhar +10 pontos (plus)
	if random.random() < 0.5:
		self.placar[self.time1 == time] += 10
		self.placar[self.time2 == time] += 10
		print("Parabéns! O jogador acertou a jogada plus! O time ganhou 10 pontos de bônus.")
	else:
		print("O jogador errou a jogada. O time mantém a mesma pontuação anterior.")


# função pra registrar a pontuação do time conforme a tabela de pontos
def registrar_pontuacao(self, time, tipo_do_ponto):
	indice_time = self.time1 == time
	self.placar[indice_time] += Tipo_de_Ponto[tipo_do_ponto]

# função pra verificar o time vencedor com base na análise da pontuação >= 90 pontos, se houve empate ou irregularidade
def time_vencedor(self, time):
	if any(pontuacao >= 90 for pontuacao in self.placar):
		return self.time1 if self.placar[0] >= 90 else self.time2

	# time1 = índice 0, time2 = índice 1
	if self.placar[0] == self.placar[1]:
		# função 'desempatar()' será chamada caso haja empate entre os times da partida
		return self.desempatar()

	# método 'aplicar.advrungh()' é chamado sempre que o time/torcida comete uma penalidade contra o adversário
	if self.houve_irregularidade:
		self.aplicar_advrungh()
		return self.time_vencedor(time)


# função que verifica se o time fez 90 pontos ou mais antes de finalizar o tempo da partida
# se o time tiver 90 pontos ou mais, o usuário poderá finalizar a partida antes do tempo encerrar (3 min.)
def time_vencedor_antes_tempo_final(self, time):
	if any(pontuacao >= 90 for pontuacao in self.placar):
		return self.time1 if self.placar[0] >= 90 else self.time2

# função pra verificar qual o time é vencedor da partida
def verificar_time_vencedor(self):
	if self.placar[0] > self.placar[1]:
		return self.time1
	elif self.placar[0] < self.placar[1]:
		return self.time2
	else:
		return self.desempatar

# função para desempatar o jogo quando encerrada a partida
def desempatar(self):
	print("Há empate ténico. Vamos descobrir quem será o vencedor com o Grito de Guerra da torcida de cada time!")
	# grito de guerra irá percorrer os dois times em disputa

	# # TIME 1 GRITA
	# TIME 2 GRITA
	# FAZER COMPARAÇÃO QUEM GRITA MAIS ALTO TIPO (GRITO DE 1 A 10, BAIXO, GRITO DE 11 A 20 MEDIO)
	# AO FINAL QUEM GRITAR MAIS ALTO É O VENCEDOR
	grito_time_vencedor = random.choice([self.time1, self.time2])
	print(f"A torcida do time {grito_time_vencedor.nome} foi a que gritou constantemente durante 1 min.!")
	# torcida vencedora no 'Grito de guerra' ganha 3 pontos pro time
	self.placar[self.time1 == grito_time_vencedor] += 3
	return grito_time_vencedor

# função pra aplicar penalidade quando tiver ocorrido por parte do time adversário ou da torcida
def aplicar_advrungh(self):
	if self.tipo_de_irregularidade == "bateu_2_vezes":
		print("O jogador cometeu irregularidade, pois bateu 2x na bola na mesma jogada.")
	elif self.tipo_de_irregularidade == "invasao_quadra":
		print("Houve irregularidade por parte da torcida adversária, porque invadiu a quadra durante o jogo.")

		penalidade_time = self.irregularidade_time
		print(f"Houve irregularidade causada pelo time {penalidade_time.nome} adversário.")
		self.placar[self.time1 == penalidade_time] -= 10
		self.placar[self.time2 == penalidade_time] -= 10
		self.houve_irregularidade = False
		return self.time_vencedor()





# função que gera a tabela de pontuação total ao final de cada partida
def gerar_tabela_final_partida(self):
	resultado_final_partida = f"O resultado da partida foi: {self.time1.nome} {self.placar[0]} vs. {self.time2.nome} {self.placar[1]}"
	return resultado_final_partida
