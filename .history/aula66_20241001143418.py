""" 
Argumentos Nomeados e NÃO Nomeados em funções Python
Nomeado: é argumento que tem nome com sinal de igual
NÃO Nomeado: é argumento que recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(x + y)
    print(f"{x=}, {y=}", "|", "x + y = ", x + y)
    
# Argumento Posicional: 1 -> x, 2 -> y    
soma(1, 2)

# Argumento Nomeado: y=2, x=1
soma(y=2, x=1)