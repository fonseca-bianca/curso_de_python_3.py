"""Função 'range' é iterável. Range + for: para usar intervalos de números
range: range(start, stop, step) ex.: range(5, 10, 2) ---> step: de qto em qto número se quer pular
"""

numeros = range(1, 10, 2)
# numeros = range(5, 10)
# numeros = range(5, 10, 2)
# print(numeros)

for numero in numeros:
    print(numero)