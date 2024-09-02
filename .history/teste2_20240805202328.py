import time 
def desempatar(self):
	#valor_grito = self.time1
	
# Contagem inicial    
    valor_grito = 0
    count = 15  
    
        
    while count >= 0:
            print(count)
            count -= 1
            time.sleep(1)  # Pausa de 1 segundo entre as contagens
    if count == 0:
        valor_grito = random.randrange(0, 10)
        print(f"Valor grito {valor_grito}")

	

	#print(random.randrange(3, 9))