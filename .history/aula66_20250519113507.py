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
    # print(x + y + z)
    # Parâmetro: vai na definição da função. É a variável
    print(f"{x=}, {y=}, {z=}", "|", "x + y + z = ", x + y + z)
    
# Argumento NÃO Nomeado/Posicional: 1, 2, 3
soma(1, 2, 3) # os argumentos são passados na ordem em que foram definidos

# Argumento Nomeado/Posicional: z=5
# Argumento Posicional: 1 -> x, 2 -> y    
soma(1, 2, z=5) # os próximos argumentos deverão ser Nomeados, pq o último é 
# Nomeado

# ERRO:
# variáveis x, y e z foram criadas apenas dentro da função soma. Elas 
# não existem fora dela, então o Python retorna:
#     NameError: name 'y' is not defined
# Em Python, variáveis definidas dentro de uma função são locais — só existem 
# e são válidas enquanto a função está sendo executada.

# Depois que a função termina, essas variáveis são descartadas da memória
# soma(y=2, x=1, z=5)
# print(y,x, z, sep="-") 

# ✅ Como resolver, se quiser usar os mesmos valores fora da função?
# Você pode:

# 1. Criar as variáveis fora da função:
# x = 1
# y = 2
# z = 5
# soma(x, y, z)
# print(y, x, z, sep="-")

# 2. Ou modificar a função para retornar os valores

# OBS.:
    # se fizer:
    # print(soma)
    # output:
    # <function soma at 0x000002931F74A340> 
        # --> ou seja, está se referindo ao nome da função na memória, não ao 
        # resultado dela