""" 
Operadores de Atribuição COM Operadores Aritméticos:
= , += , -= , *= , /= (divisão retorna nº ponto flutuante), 
//= (divisão inteira), **= (potência) , %= (módulo)
"""

contador = 0

while contador < 10:
    print(contador) 
    contador += 1
        
print("Acabou a contagem.")


contador = 10

contador *= 2 # vai multiplicar a "string" com o valor "2" pelo valor
#antigo do contador, q é 10, ou seja, o resultado será 10 números 2222222222
print(contador)

# OBS.:
#     duas variáveis contador são distintas em termos de escopo, e a 
#     alteração delas depende do local onde são usadas no código