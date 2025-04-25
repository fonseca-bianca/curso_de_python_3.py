contador = 0

while contador < 10:
    # print(contador) # vem ANTES do 'contador' ser incrementado e mostra o 
    # valor inicial do contador, por isso mostra de 0 a 10
    # contador = contador + 1 --> forma menos usual pra incrementar
    contador += 1
    print(contador) # se vier DEPOIS do 'contador', então será primeiro 
    # incrementado pra depois ser impresso
    
print("Acabou a contagem.")