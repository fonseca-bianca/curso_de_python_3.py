from datetime import datetime

class Time:
	# método construtor irá atribuir os valores dos Parâmetros aos Atributos da instância
	# (Objeto criado a partir da classe 'Time')
	def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
		self.nome = nome
		self.grito_de_guerra = grito_de_guerra
		self.ano_de_fundacao = ano_de_fundacao

	def mostrar_informacoes_times(self):
		print(f"Nome: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}")


def inserir_nome():
	times = []
	for i in range(1, 9):
		try:
			nome = input(f"Qual o nome do time {i}? ")
			if len(nome) > 10:
				print("O nome do time precisa ter, no máximo, 10 caracteres.")
		except ValueError as e:
			print(e)
		return nome

		try:
			grito_de_guerra = input(f"Qual o grito de guerra do time {i}? ")
			if len(grito_de_guerra) > 10:
				print("O grito de guerra do time precisa ter, no máximo, 20 caracteres.")
		except ValueError as e:
			print(e)
		return grito_de_guerra

		try:
			ano_de_fundacao = input(f"Qual o ano de fundação do time {i}? (Modelo de data: MM/dd/yyyy) ")
			datetime.strptime(ano_de_fundacao, "%m/%d/%Y")
		except ValueError:
			print("O modelo da data não permitido. Use o formato indicado no exemplo.")
		return ano_de_fundacao

		time = Time(nome, grito_de_guerra, ano_de_fundacao)
		times.append(time)
	return times

times = inserir_nome()
for time in times:
	time.mostrar_informacoes_times()
