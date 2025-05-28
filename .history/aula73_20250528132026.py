""" 
Higher Order Functions (Funções de Primeira Classe):
funções q podem receber e/ou retornar OUTRAS funções

DIFERENTE DE

First-Class Functions:
funções q são tratadas como outros TIPOS de dados comuns (str, int, float etc.)

Em Python, funções são consideradas "cidadãs de primeira classe".
Isso significa que você pode tratá-las como se fossem qlqr outro 
tipo de dado, como números, strings, ou listas. 
    O que vc pode fazer com uma variável, vc também pode fazer com uma função. 
    Abaixo estão os principais pontos:
"""

def saudacao(msg):
    return msg

saudacao_2 = saudacao # saudacao_2 aponta pra saudacao (referência ao q 
# está na memória)

v = saudacao_2("Bom dia")
print(v) # retorno da função sendo impresso


print("---------------------------------------------------------------------")
""" 
Explicação chatGPT:
"""

# Atribuir uma função a uma variável:
def saudacao_manha(mensagem):
    return mensagem

nova_saudacao = saudacao_manha  
# A função 'saudacao_manha' é atribuída à variável 'nova_saudacao', q agora 
# pode ser usada como uma função

print(nova_saudacao("Bom dia"))  
# chama 'nova_saudacao' com a mensagem "Bom dia", funcionando exatamente 
# como a função original

# Função que recebe outra função como argumento:
def executa_funcao(func, mensagem):
    return func(mensagem)

print(executa_funcao(nova_saudacao, "Boa tarde"))
# 'executa_funcao' recebe como PARÂMETRO (nome usado na definição da função) 
# a função 'nova_saudacao' e, como ARGUMENTO (valor passado qndo função 
# é chamada), a mensagem "Boa tarde"
# Esses valores são passados para os parâmetros 'func' e 'mensagem'
# Dentro de 'executa_funcao', a função recebida é executada com a mensagem
# como argumento


# Retornar uma função de dentro de outra função:
def criar_saudacao():
    def saudacao_interna(mensagem):
        return f"Saudação: {mensagem}"
    return saudacao_interna

saudacao_personalizada = criar_saudacao()
print(saudacao_personalizada("Olá"))
# nesse caso, a função 'criar_saudacao' retorna outra função (saudacao_interna)
# Agora, saudacao_personalizada é uma nova função q pode ser chamada mais tarde

""" 
Funções em Python são extremamente flexíveis e podem ser usadas como qualquer 
outro tipo de dado. Elas podem ser atribuídas a variáveis, passadas como 
parâmetros e retornadas de outras funções. Isso oferece uma maneira poderosa 
de estruturar seu código de forma mais dinâmica e modular.
"""