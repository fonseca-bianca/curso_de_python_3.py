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

# contador *= "2.2" # vai multiplicar a "string" com o valor "2" pelo valor
contador *= 2 
print(contador)

# OBS.:
#     duas variáveis contador são distintas em termos de escopo, e a 
#     alteração delas depende do local onde são usadas no código

# contador *= float("2.2") output: 22.0
# contador *= "2.2" output: "2.22.22.22.22.22.22.22.22.22.2"
# contador *= "2" output: "2222222222"
# contador *= 2 output: 20
