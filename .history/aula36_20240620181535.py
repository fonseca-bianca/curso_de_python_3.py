""" 
Operadores de Atribuição COM Operadores Aritméticos:
= , += , -= , *= , /= , //= , **= , %=
"""

contador = 0

while contador <= 10:
    print(contador) #vem ANTES do 'contador' ser incrementado e mostra o valor inicial do contador
    contador += 1
    # print(contador): se vier DEPOIS do 'contador', então será primeiro incrementado pra depois ser impresso
    
print("Acabou a contagem.")


contador = 10

contador *= "2"
print(contador)