def func():
    return 2

minha_funcao = func
retorno_o = minha_funcao()

print(retorno_o) # output: 2


# função passada como argumento de outra função: é a base pra criação de 
# Decoradores em Python:
def exibe_func(f):
    print(f'Objeto de função recebido: {f}')
    print(f'Nome da função: "{f.__name__}"')

exibe_func(func) 

print("---------------------------------------------------------------------")

def meu_decorador(func_funcao):
    def meu_pacote(*args, **kwargs):
        retorno = func_funcao(*args, **kwargs)
        return retorno.upper() # retorno: guarda esse resultado ("Olá, Juliano!")
    return meu_pacote

@meu_decorador
def dizer_oi(nome):
    return f'Olá, {nome}!'

print(dizer_oi('Juliano'))
# output: OLÁ, JULIANO!


# variável 'retorno': guarda o resultado ("Olá, Juliano!")
# 'Juliano' vai para *args ou **kwargs?
#   👉 Vai para *args, como uma tupla ('Juliano',)
#       (**kwargs só seria usado se você chamasse, por exemplo:
#                   dizer_oi(nome="Juliano")) (pq aq seria um Dicionário)

# meu_pacote retorna retorno, e esse retorno é func?
#   👉 meu_pacote retorna retorno.upper().
#   👉 retorno é o resultado de func(*args, **kwargs).
#   👉 Como func aponta para dizer_oi, o valor é "Olá, Juliano!".
#   👉 Depois o decorador transforma em "OLÁ, JULIANO!".

# 🔑 Resumindo:
# func → referência da função original (dizer_oi)
# retorno → variável q traz o resultado de chamar 'func'
# meu_pacote → função que envolve (wrap) a execução e devolve o resultado 
# modificado