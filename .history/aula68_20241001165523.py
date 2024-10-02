"""
Escopo de funções em Python:
significa o local onde aquele cód poderá atingir
Tipos:
a) Local:
é o escopo onde APENAS nomes do mesmo local podem ser alcançados
b) Global:
é o escopo onde TODO o cód é alcançável
OBS.: com funções, o cód consegue executar comandos em ordens distintas, SEM ser 
sempre da esquerda->direita e de cima->baixo
"""

# aq a função é apenas definida
def escopo():
    x = 1
    print(x)

# aq a função é chamada de fato
escopo()