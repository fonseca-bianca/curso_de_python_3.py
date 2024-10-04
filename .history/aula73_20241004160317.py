""" 
Higher Order Functions (Funções de Primeira Classe)
"""

def saudacao(msg):
    return msg

saudacao_2 = saudacao # saudacao_2 aponta pra saudacao (referência ao q está na memória)

v = saudacao_2("Bom dia")
print(v)