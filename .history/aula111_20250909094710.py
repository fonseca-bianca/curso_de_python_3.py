"""
Map, Partial, GeneratorType e esgotamento de Iterators

1. Funções:
    a. Map
    b. Filter
    c. Reduce



- sobre o uso de vírgulas separando cada dicionário:
    A vírgula colocada ao final de cada dicionário é chamada de "vírgula 
    pendente ou trailing comma" e é uma boa prática em Python, especialmente
    quando se trabalha com listas ou tuplas de múltiplos elementos. 

"""

from functools import partial
# O partial é usado para criar uma nova função com alguns de seus args já 
# predefinidos
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print_iter(novos_produtos)




# usando map:
print(
    list(map(
        lambda x: x * 3, 
        [1, 2, 3, 4, 5]
    ))
)
# output: [3, 6, 9, 12, 15]