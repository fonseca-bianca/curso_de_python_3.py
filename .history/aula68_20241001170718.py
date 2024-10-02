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
    print(x) # 'x' está DENTRO da função

"""aq a função é chamada de fato:
ou seja, o cód é executado de baixo pra cima, só quando a função é chamada
é q o cód é executado"""
escopo()