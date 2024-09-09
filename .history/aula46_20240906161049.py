for i in range(10): # percorre de 0 a 9
    if i == 2:
        print("i é 2, pulando...")
        continue
    
    if i == 8:
        print("i é 8, seu else não executará se houver um 'break' no código")
        continue
    
    for j in range(1, 3): #para cada valor de i (exceto quando i == 2), este loop aninhado percorre os valores de j de 1 até 2, imprimindo o par (i, j) 
        #range inclui o valor final 3, mas NÃO vai até ele
        print(i, j) #linha, coluna
        
else:
    print("Loop 'for' completado com sucesso")