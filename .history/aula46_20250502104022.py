# o cód abaixo poderia ser escrito usando o 'while', porém, neste caso, aí
# teríamos q fazer o controle manual de variável de loop

print("Usando for:")
for i in range(10): # percorre de 0 a 9
    if i == 2:
        print("i é 2, pulando...")
        continue
    
    if i == 8:
        print("i é 8, seu else não executará se houver um 'break' no código")
        continue
        # break # já iria pular pra saída q, no caso, é o print acima,
        # já q o cód abaixo NÃO iria ser executado
    
    for j in range(1, 3): # para cada valor de 'i' (exceto quando i == 2),
        # este loop aninhado percorre os valores de j de 1 até 2, 
        # imprimindo o par (i, j) 
        # valor final 3, mas é EXCLUSIVO, logo, 'j' vai percorrer até o 2
        print(i, j) # imprime linha, coluna
        
else:
    print("Loop 'for' completado com sucesso")
    
print(20*"-")

print("Usando While:")
i = 0
while i < 10:
    if i == 2:
        print("i é 2, pulando...")
        i += 1
        continue
    
    if i == 8:
        print("i é 8, seu else não executará se houver um 'break' no código")
        i += 1
        continue
        # break
    
    j = 1
    while j < 3:
        print(i, j)
        j += 1
    
    i += 1
else:
    print("Loop 'while' completado com sucesso")