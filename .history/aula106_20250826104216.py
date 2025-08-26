def func():
    return 2

minha_funcao = func
retorno = minha_funcao()

print(retorno) # output: 2

def exibe_func(f):
    print(f'Objeto de função recebido: {f}')
    print(f'Nome da função: "{f.__name__}"')

exibe_func(func) 