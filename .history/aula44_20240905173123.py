"""Função 'range' é iterável. Range + for: para usar intervalos de números
range: range(start, stop, step) ex.: range(5, 10, 2) ---> step: de qto em qto número se quer pular
Pode índices NEGATIVOS: ex.: numeros = range(0, -3, -2) ---> Retorno: 0, -2, -4, -6, -8) 
"""

numeros = range(0, 10, 2)
# numeros = range(5, 10)
# numeros = range(5, 10, 2)
# print(numeros)

for numero in numeros:
    print(numero)