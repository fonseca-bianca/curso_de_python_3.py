"""
Filtro (filter) de Dados em List Comprehensions:
    - depois do 'for' tem um 'if' e os itens podem ou não ser incluídos na 
    lista final
    - é uma função embutida (built-in) do Python
    - filtra elementos de uma sequência (lista, tupla, etc.) e mantém apenas
    os elementos q atendem a uma condição específica
    - Sintaxe:
        filter(function, iterable)
            function: vai retornar True ou False pra CADA item
            iterable: o objeto q está sendo filtrado (lista, tupla, etc.)
            RESULTADO:
                objeto do tipo filter
                pra ver o resultado, é necessário usar 'for' ou 'list()'
                
    - exemplo SEM função anônima (lambda):
        def eh_par(numero):
            return numero % 2 == 0

        numeros = [1, 2, 3, 4, 5, 6]
        pares = filter(eh_par, numeros)

        print(list(pares))  # [2, 4, 6]
        
    - exemplo COM função anônima (lambda):
        numeros = [1, 2, 3, 4, 5, 6]

        pares = filter(lambda x: x % 2 == 0, numeros)

        print(list(pares))  # [2, 4, 6]

                
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
# Lista de Dict chamada 'produtos'
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)