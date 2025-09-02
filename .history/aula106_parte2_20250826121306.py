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
    

print("---------------------------------------------------------------------")
# Decoradores com Argumentos:
def repetir_vezes(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir_vezes(3)
def dizer_oi(nome):
    print(f'Olá, {nome}!')

dizer_oi('Juliano')
# output:
# Olá, Juliano!
# Olá, Juliano!
# Olá, Juliano!