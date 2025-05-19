""" 
Argumentos Nomeados e NÃO Nomeados em funções Python:
Nomeado: é argumento que tem nome com sinal de igual
NÃO Nomeado/Posicional: é argumento que recebe apenas o argumento (valor)
OBS.: normalmente, ou usamos Nomeado OU usados NÃO Nomeado, dificilmente 
serão misturados no mesmo cód
OBS.2: execução da função: são os parênteses
"""

# definição da função:
def soma(x, y, z):
    print(x + y + z)
    # Parâmetro: vai na definição da função. É a variável
    print(f"{x=}, {y=}, {z=}", "|", "x + y + z = ", x + y + z)
    
# Argumento NÃO Nomeado/Posicional: 1, 2, 3
soma(1, 2, 3) # os argumentos são passados na ordem em que foram definidos

# Argumento Nomeado/Posicional: z=5
# Argumento Posicional: 1 -> x, 2 -> y    
soma(1, 2, z=5) # os próximos argumentos deverão ser Nomeados, pq o último é 
# Nomeado

# Argumento Nomeado: y=2, x=1
soma(y=2, x=1, z=5)
print(1, 2, 3, sep="-")