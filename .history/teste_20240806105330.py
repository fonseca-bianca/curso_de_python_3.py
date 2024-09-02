class Time:
	# método construtor irá atribuir os valores dos Parâmetros aos Atributos da instância
	# (Objeto criado a partir da classe 'Time')
	def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
		self.nome = nome
		self.grito_de_guerra = grito_de_guerra
		self.ano_de_fundacao = ano_de_fundacao


def nome():
	nome = input(f"Qual o nome do time1? {nome}\n")
	return nome
	