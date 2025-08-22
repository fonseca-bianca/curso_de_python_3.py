"""
Adiando a execução de funções (Closure):
    Pra fazer isso, precisamos 'Decorar' a função.
    Decorar uma função significa modificá-la ou envolver seu comportamento 
usando um decorator (uma função que recebe outra função como arg e retorna 
uma nova função).

📌 Exemplo simples:

def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador   # aqui a função é "decorada" (semelhante às @nnotations em 
Java)
def diga_ola():
    print("Olá!")

diga_ola()


Output:
Antes da função
Olá! # aqui a função foi decorada
Depois da função


👉 Ou seja, “decorar” é aplicar lógica extra sem mudar o código original da função.

Quer que eu te mostre como usar isso em algo prático, tipo medir o tempo de execução de uma função?
"""

# def soma(x, y):
#     return x + y

# def multiplica(x, y):
#     return x * y

# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# def externa(x):
#     def interna(y):
#         return x + y
#     return interna

# soma_com_cinco = externa(5)
# print(soma_com_cinco(10))

# print("---------------------------------")

# def externa_2(x):
#     def interna_2(y):
#         return x * y
#     return interna_2 

# multiplica_por_dez = externa_2(10)
# print(multiplica_por_dez(5))


def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def externa(operacao, x): # devolve a interna criando o closure
    def interna(y): # é quem usa operacao(x, y) e executa a soma, multiplic.
        return operacao(x, y) # 'operacao': aponta para a função 
#    (soma ou multiplica)
    return interna

soma_com_cinco = externa(soma, 5)
print(soma_com_cinco(10))
# 15

multiplica_por_dez = externa(multiplica, 10)
print(multiplica_por_dez(5))
# 50