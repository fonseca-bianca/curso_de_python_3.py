contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6 or contador == 8:
        print("Não vou mostrar o número 6")
        continue
    
    print(contador)
    
    if contador == 12:
        break

print("Acabou a contagem")