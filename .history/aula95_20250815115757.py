"""
Raise: lançamento de Exceções (erros)
https://docs.python.org/3/library/exceptions.html
"""


def nao_pode_zero():
    if d == 0:
        raise ZeroDivisionError("Não pode dividir por zero")
    return True # se o número q está dividindo NÃO for zero