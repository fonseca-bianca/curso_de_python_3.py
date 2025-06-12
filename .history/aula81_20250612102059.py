""" Introdução à função lambda (função anônima de uma linha):
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
lista.sort(reverse=True) # inverte a ordem da lista, ordenando-a em ordem 
# decrescente
sorted(lista)

OBS.:
sorted() faz shadow copy da lista original, 
    é uma função built-in do Python (embutida)
    usada com QLQR iterável (list, tuple, set, dict, etc)
    NÃO modifica o iterável original
    retorna um NOVO iterável ordenado

                    DIFERENTE DE

sort() modifica a lista original (faz deeep copy):
    é um método de LISTA (somente)
    modifica somente a LISTA
    retorna None
"""
from numpy.ma.core import logical_or
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort() # ordena a lista em ordem crescente
print(lista)

# ou

lista2 = [1, 20, 18, 31, 7, 12, 100, 30]
lista2 = sorted(lista2)  
# Atribuindo essa nova lista (lista2) de volta à variável lista2, 
# sobrescrevendo o conteúdo anterior dela q era uma lista NÃO ordenada,
# agora, com a sobrescrita, ela passa a ser uma lista ordenada
# OBS.:
    # como sobrescrevi a variável lista2, a lista original foi perdida, logo, 
    # eu só consigo ver o novo valor. Caso eu quisesse manter a lista original,
    # eu poderia fazer algo como:
    #     lista2_original = lista2.copy()  # Faz uma cópia da lista original
    #     # ou
    #     lista2_original = lista2[:]  # Outra forma de fazer cópia da lista

print(lista2)


print()
print('Função lambda:')

lista_nomes = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

