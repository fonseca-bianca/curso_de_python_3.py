"""
EXERCÍCIO EM FUNÇÕES
Crie uma função que multiplica todos os argumentos NÃO nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
Crie uma função que fale se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
import math

def multiplica_todos(*args): 
    return math.prod(args)

resultado = multiplica_todos(1, 2, 3, 4, 5, 6, 7)
print(resultado)