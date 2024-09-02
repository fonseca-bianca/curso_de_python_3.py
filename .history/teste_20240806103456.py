def excluir_time(times, nome):
	if nome in times:
		del times[nome]
		print(f"O time {nome} foi excluido com sucesso!")
	else:
		print(f"O nome do time {nome} não foi encontrado no sistema. Digite o nome do time novamente.")
