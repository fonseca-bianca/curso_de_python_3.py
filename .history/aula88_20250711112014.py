"""
Valores Falsy, Tipos Mutáveis e Imutáveis:
    - Mutáveis: [lista], {dict}, set()
    - Imutáveis: (tupla), "" (str vazia), 0, 0.0, False, None, range(0)

Valores Truthy, Tipos Mutáveis e Imutáveis:
    - Mutáveis: [lista], {dict}, set([10])
    - Imutáveis: (tupla), " " (str com espaço ou letras), 1, 0.1, True, 
        range(0, 10)
"""

lista = []
tupla = ()
dicionario = {}
conjunto = set()
string = ""
inteiro = 0
flutuanete = 0.0
booleano = False
nulo = None
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f"{lista} é falsy{lista}")