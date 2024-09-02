

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

		time = Time(nome)
		times.append(time)
	return times

times = inserir_nome()
for time in times:
	time.mostrar_informacoes_times()