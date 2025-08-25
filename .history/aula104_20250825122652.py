"""
...continuação aula 103
com complemento:
@syntactic_sugar (Açúcar Sintático - Decorador em Python): 
   - O @ é só uma forma mais limpa, curta e legível de aplicar o decorator.

"""

def criar_funcao(func): # função decoradora q recebe como arg outra função
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao #syntactic sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

# COM Syntactic Sugar (@):
# o próprio Python traduz a linha com o Decorador:
#           'def inverte_string(string):'
# o Python vai transformar o Decorador em: 
#           'inverte_string = criar_funcao(inverte_string)'
# o Decorador EVITA q tenha q escrever no cód o trecho:
#           'func = decorator(func)'
#                pra avisar q é um Decorador


# SEM açúcar sintático (@):
# Se você NÃO usasse o @, ficaria assim manualmente:
# 
# def inverte_string(string):
#     print(f'{inverte_string.__name__}')
#     return string[::-1]

# inverte_string = criar_funcao(inverte_string)  # <-- decoração manual
# OU SEJA,
# pegar 'inverte_string' e SUBSTITUIR pela versão decorada 'criar_funcao()'


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)