""" 
Higher Order Functions (Funções de Primeira Classe)
"""

def saudacao(msg):
    return msg

saudacao_2 = saudacao # saudacao_2 aponta pra saudacao (referência ao q está na memória)

v = saudacao_2("Bom dia")
print(v)


"""Em Python, funções são consideradas "cidadãs de primeira classe".
Isso significa que você pode tratá-las como se fossem qualquer outro 
tipo de dado, como números, strings, ou listas. O que você pode fazer 
com uma variável, você também pode fazer com uma função. Aqui estão os 
principais pontos:"""


print("-----------------------------------------------------------------------")
""" 
Explicação chatGPT:
"""

# Atribuir uma função a uma variável:
def saudacao_manha(mensagem):
    return mensagem

nova_saudacao = saudacao_manha  # Atribuímos a função a uma nova variável
print(nova_saudacao("Bom dia"))  # Funciona como a função original

# Passar uma função como argumento para outra função:
def executa_funcao(func, mensagem):
    return func(mensagem)

print(executa_funcao(saudacao_manha, "Boa tarde"))
# aq a função 'executa_funcao' recebe uma função (func) e um argumento para 
# essa função (mensagem). A função passada (saudacao) é então executada dentro 
# de executa_funcao.

# Retornar uma função de dentro de outra função:
def criar_saudacao():
    def saudacao_interna(mensagem):
        return f"Saudação: {mensagem}"
    return saudacao_interna

saudacao_personalizada = criar_saudacao()
print(saudacao_personalizada("Olá"))
# nesse caso, a função criar_saudacao retorna outra função (saudacao_interna). Agora, saudacao_personalizada é uma nova função que pode ser chamada mais tarde.