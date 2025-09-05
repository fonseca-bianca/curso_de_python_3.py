"""
Combinations, Permutations e Product - itertools

* Combinations:
    Retorna todas as combinações possíveis de um iterável, SEM repetição.
    ordem NÃO importa
    recebe:
        iterável + tamanho da combinação
    Ex.: combinations([1, 2, 3], 2) -> (1, 2), (1, 3), (2, 3)
    EX.: joão, joana
        retorna:
            joão, joana
            NÃO retorna joana, joão
    

** Permutations:
    Retorna todas as permutações possíveis de um iterável, COM repetição.
    ordem IMPORTA
    recebe:
        iterável + tamanho da permutação
    Ex.: permutations([1, 2, 3], 2) 
    -> (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
    EX.: joão, joana
        retorna:
            joão, joana
            RETORNA tbm joana, joão
    

*** Product:
    Retorna o produto cartesiano de dois ou mais iteráveis.
    ordem IMPORTA e REPETE valores únicos
    recebe:
        iteráveis
    Ex.: product([1, 2], [3, 4]) -> (1, 3), (1, 4), (2, 3), (2, 4)

** Itertools **: 
    é módulo padrão do Python e alberga várias funções q criam
    iteradores de forma mais eficiente no código
"""

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

pessoas = [
    "João", "Joana", "Luiz", "Letícia"
]

camisetas = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", "unissex"],
    ["algodão", "poliéster"]
]

# print(combinations(pessoas, 2))
# output: SE NÃO houver a função print_iter acima: 
# <itertools.combinations object at 0x0000028943002C50>

print_iter(combinations(pessoas, 2))
# NÃO repete:
# ('João', 'Joana')
# ('João', 'Luiz')
# ('João', 'Letícia')
# ('Joana', 'Luiz')
# ('Joana', 'Letícia')
# ('Luiz', 'Letícia')

print_iter(permutations(pessoas, 2))
# Repete:
# ('João', 'Joana')
# ('João', 'Luiz')
# ('João', 'Letícia')
# ('Joana', 'João')
# ('Joana', 'Luiz')
# ('Joana', 'Letícia')
# ('Luiz', 'João')
# ('Luiz', 'Joana')
# ('Luiz', 'Letícia')
# ('Letícia', 'João')
# ('Letícia', 'Joana')
# ('Letícia', 'Luiz')


print_iter(product(*camisetas))


# print(*list(iterator), sep="\n"):
#   list(iterator): Primeiro, ela converte o iterador que recebe em uma lista. 
#   Isso é necessário porque iteradores só podem ser consumidos uma vez. 
#   Ao convertê-lo para uma lista, você "captura" todos os itens para poder 
#   imprimi-los.
# *: 
#   O asterisco (operador de desempacotamento ou unpacking) "desempacota" 
#   cada item da lista como um argumento individual para a função print(). 
#   Por exemplo, print(*[1, 2, 3]) é o mesmo que print(1, 2, 3).
# sep="\n": 
#   Este argumento diz para a função print() usar uma nova linha (\n) como 
#   separador entre cada item desempacotado. Isso faz com que cada combinação, 
#   permutação ou produto seja impresso em uma linha separada, facilitando a 
#   leitura.
#
# print_iter(product(*camisetas)):
#   camisetas é uma lista de listas. Ou seja, é um iterável que contém outros 
#   iteráveis
#   O asterisco * antes de camisetas é o mesmo operador de desempacotamento que
#   vimos acima. Ele pega cada lista dentro de camisetas e a "desempacota" como 
#   um argumento separado para a função product()