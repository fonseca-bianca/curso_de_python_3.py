contador = 0

while contador < 10:
    # print(contador) # vem ANTES do 'contador' ser incrementado e mostra o 
    # valor inicial do contador, por isso mostra de 0 a 10
    # contador = contador + 1 --> forma menos usual pra incrementar
    contador += 1
    print(contador) # se vier DEPOIS do 'contador', então será primeiro 
    # incrementado pra depois ser impresso, logo, mostrará de 1 a 10
    
print("Acabou a contagem.")

# OBS.:
#     print(contador) ANTES do incremento:
#         Imprime antes de somar.
#         Resultado: 0 1 2 ... 9
#         Útil quando você quer mostrar o valor antes da mudança
        
#     print(contador) DEPOIS do incremento:
#         Soma antes de imprimir.
#         Resultado: 1 2 3 ... 10
#         Útil quando você quer mostrar o valor depois da mudança.
    
    #   while contador < 10:
    #     print(contador) ANTES do contador:
    #         neste caso, vai imprimir de 0 a 9
    #   while contador <= 10:
    #     print(contador) ANTES do contador:
    #         neste caso, vai imprimir de 0 a 10
    
    #   while contador < 10:
    #     print(contador) DEPOIS do contador:
    #         neste caso, vai imprimir de 0 a 9
    #   while contador <= 10:
    #     print(contador) DEPOIS do contador:
    #         neste caso, vai imprimir 1 a 11