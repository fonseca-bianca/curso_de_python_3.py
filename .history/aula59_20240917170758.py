"""
Desempacotamento em chamadas:
chamadas de métodos e funções
"""

string_letra = "ABCD"
lista_nomes = ["Amy Lee,", "Kurt Cobain", "Axl Rose", 1, 2, 3]
tupla_frase = "Python", "é", "legal"

a, b, c, d, *_ = lista_nomes # itens da lista (Amy Lee, Kurt Cobain, Axl Rose)
print(a, c) # a = Amy Lee, c = Axl Rose