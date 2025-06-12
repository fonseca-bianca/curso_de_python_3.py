""" Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer outra em Python. Porém, é função 
anônima que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de 
uma única expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort(reverse=True)
sorted(lista)
"""
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort() # ordena a lista em ordem crescente
print(lista)

# ou

lista2 = [1, 20, 18, 31, 7, 12, 100, 30]
sorted(lista2)
print(lista2)