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
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_valor_triplicado = list(map(
    lambda p: {**p, 'preco': p['preco'] * 3},
    produtos
))


for produto in produtos:
    print(f"{produto['nome']} com valor original: R${produto['preco]']}")
    
for produto in produtos_valor_triplicado:
    print(
        f"{produto['nome']} com valor triplicado:\n"
        f"R${produto['preco']:.2f}"
    )