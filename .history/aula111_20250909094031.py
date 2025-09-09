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

produtos = [
    {'nome': 'Produto 5', 'preco': 10.0},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.9},
]

def aumentar_dez_por_cento(valor, porcentagem):
    return round(valor * porcentagem, 2)

novos_produtos = [
    {**p,
     'preco': aumentar_dez_por_cento(p['preco'])}
    for p in produtos
]





# usando map:
print(
    list(map(
        lambda x: x * 3, 
        [1, 2, 3, 4, 5]
    ))
)
# output: [3, 6, 9, 12, 15]