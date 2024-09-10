"""Introdução às Listas Mutáveis em Python
Tipo: list (é mutável)
suporta muitos tipos de valores
índices e fatiamento (reutilização de cód) 
Métodos: .append(), insert, pop, del, clear, extend e etc.
"""

# type: mostra o tipo de valores
string = "abc" # seus índices poderiam ser percorridos pela função (len())
minha_lista = ['123', True, "Ana Maria", 1.2, []] # é o mesmo que uma string vazia ""
print(minha_lista)

# print(bool(minha_lista)) # falsy: quando uma lista está vazia ela é SEMPRE false
# print(minha_lista, type(minha_lista))