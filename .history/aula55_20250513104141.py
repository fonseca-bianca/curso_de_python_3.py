"""Imprecisão números float + round e decimal:
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(numero3)
print(type(f"{numero3:.2f}")) 
# vai imprimir somente 2 casas após o ponto = 0.80, pq aq retorna uma STRING
# dois pontos: realiza a formatação no valor da variável 'numero3' dentro da 
# f-string

# Usando Função round():
#     recebe a variável possui o valor float q se quer arredondar
#     1º argumento: a variável
#     2º argumento: o número de casas decimais q se quer arredondar
#     print(round(numero3, 1))
#     print(type(numero3))
#     vai imprimir somente 1 casa após o ponto = 0.8, pq aq retorna um FLOAT


""" DECIMAL IMPORT:
Corrige o problema de imprecisão em números decimais muito grandes.
Ex.: 0.1 + 0.7 = 0.7999999999999999

    round(numero3, 1) → 0.8 (1 casa decimal)

    round(numero3, 2) → 0.80 (2 casas decimais)

É ideal pra cálculos financeiros, pois o round() não é preciso.

Ex.:

import decimal  # Módulo

numero1 = decimal.Decimal('0.1')  
numero2 = decimal.Decimal('0.7')  
numero3 = numero1 + numero2  
print(numero3)

OBS:
    - decimal = módulo decimal
    - Decimal = classe disponível dentro do módulo

Dica:
Use strings em vez de floats, pois Decimal converte corretamente uma string para número decimal com precisão.

Ex.:

numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
"""