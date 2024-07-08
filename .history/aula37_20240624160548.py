contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6 or contador == 8:
        msg_personalizada = "Não vou mostrar o número {}"
        msg_formatada = msg_personalizada.format(contador)
        print(msg_formatada)
        continue
    
    print(contador)
    
    if contador == 12:
        break

print("Acabou a contagem")