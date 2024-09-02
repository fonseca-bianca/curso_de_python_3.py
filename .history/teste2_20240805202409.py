import time 

	
	
   
    valor_grito = 0
    count = 15  
    
        
    while count >= 0:
            print(count)
            count -= 1
            time.sleep(1)  
    if count == 0:
        valor_grito = random.randrange(0, 10)
        print(f"Valor grito {valor_grito}")

	

	