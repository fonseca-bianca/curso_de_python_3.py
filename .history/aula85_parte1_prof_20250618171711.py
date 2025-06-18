"""
Filtro (filter) de Dados em List Comprehensions:
     
"""
# cód professor:
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Serve para imprimir objetos de forma bonita (estruturada).
# Usa o módulo pprint (pretty print).
# sort_dicts=False: mantém a ordem dos dicionários.
# width=40: limita a largura da impressão.


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)
# Cria uma lista com os números de 0 a 9 (SEM List Comprehension)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)
# Cria uma lista com os números de 0 a 9 (COM List Comprehension)

# Mapeamento de dados em list comprehension
# Lista de Dict chamada 'produtos' (nome e preço)
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Mapeamento com modificação condicional:
# Para cada produto:
# Se o preco > 20, cria um novo dicionário, copiando tudo e aumentando o preço 
# em 5%
# Se NÃO, só copia o produto original
#  {**produto}: faz uma cópia do dicionário
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]


# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]


# Mesma lógica, mas com filtro final no for:
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)

# A mesma modificação condicional que antes.
# MAS, só entra na lista se:
#   o preço for maior ou igual a 20, E
#   mesmo com o aumento, o novo preço for maior que 10.