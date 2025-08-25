"""
...continuando o conceito de Decoradores em Python:
HIGH ORDER FUNCTION (Função de Ordem Superior):
    função que recebe OU retorna outra função como parâmetro

DECORADOR:
    podemos modificar o funcionamento da função atual modificando os parâmetros
"""

def validar(funcao_como_argumento):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("X e Y não podem ser negativos")
        x *= 2
        y *= 2
        return funcao_como_argumento(x, y)
    return valida

@validar
def somar_dois_valores(x, y):
    return x + y

print(somar_dois_valores(10,20))