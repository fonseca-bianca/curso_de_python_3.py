from datetime import datetime

class TimeQuadribol:
	# método construtor irá atribuir os valores dos Parâmetros aos Atributos da instância
	# (Objeto criado a partir da classe 'Time')
	
		def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
			self.nome = nome
			self.grito_de_guerra = grito_de_guerra
			self.ano_de_fundacao = ano_de_fundacao

		def mostrar_informacoes_times(self):
			print(f"Nome do time: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}")


def inserir_dados():
	# lista de 'times = []': inicia vazia pra receber os times e seus respectivos atributos
	times = []
	#times de 1 a 8
	for i in range(1, 9):
		while True:
			try:
				nome = input(f"Qual o nome do time {i}? ")
				if len(nome) <= 10:
					print(f"O nome do time {i} é: {nome}")
					break
				# raise: é a palavra-chave pra gerar Exceção. Se houver, vai pra validação do 'except'
				raise Exception
			except Exception:
				print("O nome do time precisa ter, no máximo, 10 caracteres.")

		while True:
			try:
				grito_de_guerra = input(f"Qual o grito de guerra do time {i}? ")
				if len(grito_de_guerra) <= 20:
					print(f"O grito de guerra do time {i} é: {grito_de_guerra}")
					break
				raise Exception
			except Exception:
				print("O grito de guerra do time precisa ter, no máximo, 20 caracteres.")

		while True:
			try:
				ano_de_fundacao = input(f"Qual o ano de fundação do time {i}? (Modelo de data: MM/dd/yyyy) ")
				datetime.strptime(ano_de_fundacao, "%m/%d/%Y")
				break
			except:
				print("O modelo de data não permitido. Use o formato indicado no exemplo.")

		# 'time': é uma variável que recebe a classe 'Time' com seus atributos
		# 'time' logo, é um Objeto criado -> o mesmo que Instância da classe Time
		# construtor da classe Time e seus aributos são chamados e inicializados
		time = TimeQuadribol(nome, grito_de_guerra, ano_de_fundacao)
		# instância 'time' da classe criada acima é incluída na lista de 'times'
		# lista 'times' irá armazenar todas as instâncias da classe que forem criadas durante a execução do programa
		times.append(time)

		# retorna a lista com todas as instâncias criadas e adicionadas à própria lista de 'times = []'
	return times

# lista de 'times' chama a função 'inserir_dados()' com os respectivos valores incluídos em cada time
times = inserir_dados()
# laço que irá iterar (adicionar) cada novo time criado à lista de 'times' já existentes
for time in times:
	time.mostrar_informacoes_times()

