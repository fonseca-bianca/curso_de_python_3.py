contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6 or contador == 8:
        # msg_personalizada = "Não vou mostrar o número {}"
        # msg_formatada = msg_personalizada.format(contador) #vai mostrar a msg conforme cada número 6 e 8, mesmo tendo criado um único print 
        # print(msg_formatada)
        #OU
        print("Não vou mostrar o número", contador) #vai mostrar a msg conforme cada número 6 e 8, mesmo tendo criado um único print 
        continue
    
    print(contador)
    
    if contador == 12:
        break

print("Acabou a contagem")