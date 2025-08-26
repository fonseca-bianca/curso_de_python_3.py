"""
...continuação:
Ordem de aplicação dos Decoradores:
"""

# múltiplos Decoradores:

def maiuscula(func):
    def wrapper(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return wrapper

def repetir(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 3
    return wrapper

@repetir
@maiuscula
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Anna"))
    