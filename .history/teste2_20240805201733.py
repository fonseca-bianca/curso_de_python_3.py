import time 
def desempatar(self):
	valor_grito = self.time1
	

	count = 15  # Contagem inicial

	try:
		while count >= 0:
			print(count)
			count -= 1
			time.sleep(1)  # Pausa de 1 segundo entre as contagens
	except KeyboardInterrupt:
		print("Contagem interrompida manualmente.")

	print("Contagem regressiva completa.")

	print(random.randrange(3, 9))