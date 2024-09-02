import re

class Time:
	# método construtor irá atribuir os valores dos Parâmetros aos Atributos da instância
	# (Objeto criado a partir da classe 'Time')
	def __init__(self, nome, grito_de_guerra, ano_de_fundacao, cor_do_uniforme, pontuacao_do_time):
		self.nome = nome
		self.grito_de_guerra = grito_de_guerra
		self.ano_de_fundacao = ano_de_fundacao
		self.cor_do_uniforme = cor_do_uniforme
		self.pontuacao_do_time = pontuacao_do_time

# função para validação das regras do 'nome' do time
def validacao_do_nome(nome):
	if not nome:
		raise ValueError("O nome do time não pode estar vazio.")
	if len(nome) > 10:
		raise ValueError("O nome do time pode conter mais do que 10 caracteres.")
	if not nome.isalnum():
		raise ValueError("O nome do time pode conter somente letras maiúsculas, minúsculas e/ou números (de 0 a 9). "
						 "Não são permitidos caracteres especiais (*, !, ?)")

# função pra cadastrar o time
def cadastrar_time():
	times = []
	# ocorre a iteração, pois são cadastrados mais de um time (8 total)
	for i in range(8):
		# loop 'while' como 'True' pra garantir q os dados inseridos sejam válidos
		while True:
			try:
				nome = input(f"Digite o nome do time {i + 1}: ")
				validacao_do_nome(nome)
				break
			except ValueError as e:
				print(e)

		while True:
			try:
				grito_de_guerra = input(f"Digite o grito de guerra do time{i + 1}: ")
				if not grito_de_guerra.isalpha() or len(grito_de_guerra) > 20:
					raise ValueError("O grito de guerra digitado é inválido, pois deverá conter somente letras maiúsculas e/ou minúsculas ")
				break
			except ValueError as e:
				print(e)

		while True:
			try:
				ano_de_fundacao = input(f"Digite o ano de fundação do time {i + 1} (MM/dd/yyyy): ")
				# validação pra verificar se o formato da data digitado pelo usuário é o formato aceito pelo sistema
				if not re.match(r"^\d{2}/\d{2}/\d{4}$", ano_de_fundacao):
					raise ValueError("Formato de data inválido. Utilize o formato MM/dd/yyyy.")
				break
			except ValueError as e:
				print(e)

# função pro usuário selecionar a cor do uniforme do time conforme o menu de cores disponibilizadas pelo sistema
def cor_do_uniforme():
	cores_permitidas = {
		1: "rosa",
		2: "roxo",
		3: "azul",
		4: "vermelho",
		5: "laranja",
		6: "preto",
		7: "branco",
		8: "amarelo",
		9: "verde"
	}
	while True:
		try:
			print("Escolha a cor do uniforme: ")
			for numero, cor in cores_permitidas.items():
				print(f"{numero}: {cor}")
			opcao_de_cor = int(input("Escolha a cor do uniforme com base em uma das opções: "))
			return cores_permitidas[opcao_de_cor]
		# exceções lançadas caso o usuário digite um número que não condiz com os da lista de cores,
		# bem como se ele digitar outra coisa que não seja um número
		except (ValueError, KeyError):
			print("Você pode escolher somente uma cor de uniforme.")

# função pra listar os times cadastrados
def lista_de_times(times):
	if not times:
		print("O time não está cadastrado no sistema.")
		return

		print("\nLista de times: ")
		for nome, time in times.items():
			print(f"Nome do time: {time.nome}")
			print(f"Grito de guerra do time: {time.grito_de_guerra}")
			print(f"Ano de fundação do time: {time.ano_de_fundacao}")
			print(f"Cor do uniforme do time: {time.cor_do_uniforme}")
			print(f"Pontuação do time: {time.pontuacao_do_time}")
			#inclusão hífens pra separar informações de cada time
			print("-" * 20)

# função pra buscar os times pelo 'nome'
# após a busca, são trazidos os Parâmetros do Objeto (construtor da classe) 'Time' que são os Atributos da Classe 'Time'
def buscar_time(times, nome):
	if nome in times:
		time = times[nome]
		print(f"Informações do time: {time.nome}, {time.grito_de_guerra}, {time.ano_de_fundacao}, {time.cor_do_uniforme}, {time.pontuacao_do_time}")
	else:
		print(f"O time {nome} não foi encontrado.")

# função que exclui um time incluso no dicionário de times (o mesmo que Switch Case em Java)
def excluir_time(times, nome):
	if nome in times:
		del times[nome]
		print(f"O time {nome} foi excluido com sucesso!")
	else:
		print(f"O nome do time {nome} não foi encontrado no sistema. Digite o nome do time novamente.")

		# #criação do objeto 'time' e adicionar as regra dele à lista
		# t = time(nome, grito_de_guerra, ano_de_fundacao, cor_do_uniforme)
		# times.append(t)

	return times
