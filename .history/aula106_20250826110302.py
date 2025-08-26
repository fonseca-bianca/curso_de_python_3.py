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
        return retorno.upper()
    return meu_pacote

@meu_decorador
def dizer_oi(nome):
    return f'Olá, {nome}!'

print(dizer_oi('Juliano'))
# output: OLÁ, JULIANO!