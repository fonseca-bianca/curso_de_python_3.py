""" 
Argumentos Nomeados e NÃO Nomeados em funções Python
Nomeado: é argumento que tem nome com sinal de igual
NÃO Nomeado: é argumento que recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(x + y + z)
    # Parâmetro: vai na definição da função
    print(f"{x=}, {y=}, {z=}", "|", "x + y + z = ", x + y + z)
    
# Argumento: vai no valor do argumento
# Argumento Posicional: 1 -> x, 2 -> y    
soma(1, 2, z=5)

# Argumento Nomeado: y=2, x=1
soma(y=2, x=1, z=5)
print(1, 2, 3, sep="-")