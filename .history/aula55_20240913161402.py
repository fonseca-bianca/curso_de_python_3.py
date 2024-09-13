"""Imprecisão números float + round e decimal
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(numero3)
print(f"{numero3:.2f}") #vai imprimir somente 2 casas após o ponto
#dois pontos: realiza a formatação no valor da variável 'numero3' dentro da f-string

"""Função round()
recebe a variável possui o valor float q se quer arredondar
1º argumento: a variável
2º argumento: o número de casas decimais q se quer arredondar"""
print(round(numero3, 0))