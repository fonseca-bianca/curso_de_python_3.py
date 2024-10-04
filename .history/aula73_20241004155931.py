""" 
Higher Order Functions (Funções de Primeira Classe)
"""

def saudacao(msg):
    return msg

saudacao_2 = saudacao

v = saudacao_2("Bom dia")
print(v)