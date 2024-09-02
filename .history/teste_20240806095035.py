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
