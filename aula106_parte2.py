"""
...continuação:
Ordem de aplicação dos Decoradores:
    são aplicados de baixo pra cima:
    @repetir --> aplicado em 2º lugar
    @maiuscula --> aplicado em 1º lugar
"""

# múltiplos Decoradores aplicados em uma função:
def maiuscula(func): # Decorador para deixar a string em maiúsculas
    def wrapper(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return wrapper

def repetir(func): # Decorador para repetir a string 3 vezes
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 3
    return wrapper

@repetir 
@maiuscula
def saudacao(nome): # ambos @decoradores aplicados nesta função
    return f"\nOlá, {nome}!"

print(saudacao("Anna"))
    