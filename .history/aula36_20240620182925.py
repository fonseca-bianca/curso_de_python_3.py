""" 
Operadores de Atribuição COM Operadores Aritméticos:
= , += , -= , *= , /= , //= (divisão inteira e tbm uso da variável com o resultado da divisão)
, **= (potência) , %= (módulo)
"""

contador = 0

while contador <= 10:
    print(contador) #vem ANTES do 'contador' ser incrementado e mostra o valor inicial do contador
    contador += 1
    # print(contador): se vier DEPOIS do 'contador', então será primeiro incrementado pra depois ser impresso
    
print("Acabou a contagem.")


contador = 10

contador *= "2" #vai multiplicar a "string" pelo valor antigo do contador, q é 10
print(contador)