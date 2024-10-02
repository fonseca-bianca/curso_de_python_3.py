""" 
Argumentos Nomeados e NÃO Nomeados em funções Python
Nomeado: é argumento que tem nome com sinal de igual
NÃO Nomeado: é argumento que recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(x + y)
    print(f"{x=} + {y=}", "|", "x + y= ", x + y)
    
soma(1, 2)
# Argumento posicional: 1 -> x, 2 -> y