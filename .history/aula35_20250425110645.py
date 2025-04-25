contador = 0

while contador <= 10:
    print(contador) # vem ANTES do 'contador' ser incrementado e mostra o 
    # valor inicial do contador, por isso mostra de 0 a 10
    # contador = contador + 1 --> forma menos usual pra incrementar
    contador += 1
    # print(contador) # se vier DEPOIS do 'contador', então será primeiro 
    # incrementado pra depois ser impresso, logo, mostrará de 1 a 10
    
print("Acabou a contagem.")

# OBS.: sobre operador lógico:
    #   while contador < 10:
    #     print(contador) ANTES do contador:
    #         neste caso, vai imprimir de 0 a 9 (PQ CONTA 10 ELEMENTOS)
    #   
    # while contador <= 10:
    #     print(contador) ANTES do contador:
    #         neste caso, vai imprimir de 0 a 10
    
    #   while contador < 10:
    #     print(contador) DEPOIS do contador:
    #         neste caso, vai imprimir de 1 a 10
    #   
    # while contador <= 10:
    #     print(contador) DEPOIS do contador:
    #         neste caso, vai imprimir 1 a 11 (PQ CONTA 10 ELEMENTOS)

# OBS. sobre ordem do print():
#     print(contador) ANTES do incremento:
#         Imprime antes de somar.
#         Resultado: 0 1 2 ... 9
#         Útil quando você quer mostrar o valor antes da mudança

#       * Quando usar print(contador) antes do contador += 1:
#           * Imprime o valor atual do contador antes de somar
#           * Ideal quando se quer incluir o valor inicial (ex: começar do 0)

        
#     print(contador) DEPOIS do incremento:
#         Soma antes de imprimir.
#         Resultado: 1 2 3 ... 10
#         Útil quando você quer mostrar o valor depois da mudança.

#       * Quando usar print(contador) depois do contador += 1:
#           * Você soma primeiro, depois imprime.
#           * Ideal quando quer começar do próximo valor (ex: começar do 1).

# OBS.: sobre 'while' e ordem de incremento:
#  A condição do while controla quando sair do laço,
#  Mas a ordem entre incremento e print() decide quais valores você vê.