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
flutuante = 0.0
booleano = False
nulo = None
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

# Se o usuário digita um falsy (ex: "", 0, [], None), o not valor vira True
# → Ou seja, o código entra no if ou retorna 'falsy'

# Se o usuário digita um truthy (ex: "Ana", 123, [1, 2]), o not valor vira 
# False
# → Ou seja, o código vai para o else ou retorna 'truthy'

print(f"{lista=}", falsy(lista))
print(f"{tupla=}", falsy(tupla))
print(f"{dicionario=}", falsy(dicionario))
print(f"{conjunto=}", falsy(conjunto))
print(f"{string=}", falsy(string))
print(f"{inteiro=}", falsy(inteiro))
print(f"{flutuante=}", falsy(flutuante))
print(f"{booleano=}", falsy(booleano))
print(f"{nulo=}", falsy(nulo))
print(f"{intervalo=}", falsy(intervalo))
