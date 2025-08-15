"""
Raise: lançamento de Exceções (erros)
https://docs.python.org/3/library/exceptions.html
"""


def nao_pode_zero(d):
    if d == 0:
        raise ZeroDivisionError("Não pode dividir por zero")
    return True # se o número q está dividindo NÃO for zero

def num_deve_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n(float, int)):
        raise TypeError(f"'{n}' deve ser int ou float"
                        f"'{tipo_n.__name__}' foi enviado"
        )
        
    return False # se as condições dentro do 'raise' NÃO forem atendidas


def divide(n, d):
    num_deve_int_ou_float(n)
    num_deve_int_ou_float(d)
    nao_pode_zero(d)
    return n/d