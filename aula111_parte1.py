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

# função auxiliar q vai imprimir os iterators de uma lista
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


# cada dicionário é um produto
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# essa é a função q contém a lógica de aumentar o preço e considera o valor
# com 2 casas decimais
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# função partial: usada pra criar NOVA função 'aumentar_dez_por_cento'
# tem como arg 'porcentagem' fixo em 1.1 (10% de aumento)
# porcentagem é um parâmetro nomeado (keyword argument) com valor fixo
aumentar_dez_por_cento = partial(
    aumentar_porcentagem,
    porcentagem = 1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


# função central do mapeamento:
# recebe um produto, cria um NOVO dicionário com o preço daquele produto 
# atualizado (esse novo dict é cópia do dict original, mas com preço atualiz.)
# calcula o NOVO valor usando a função 'aumentar_dez_por_cento'
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_por_cento(
            produto['preco']
        )
    }


# parte MAIS IMPORTANTE:
# map vai pegar função 'muda_preco_de_produtos' e vai aplicar a cada item da
# lista 'produtos'
# resultado: é um obj map(iterator) q será convertido em uma lista (com uso do
# list()) e irá gerar uma NOVA lista (novos_produtos) com os preços atualiz.
novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


# funções auxiliares:
# print_iter e irá exibir os produtos com valores originais e os produtos com
# valores atualizados
print_iter(produtos)
print_iter(novos_produtos)




# usando função lambda (anônima) com map:
# lambda aplicada a cada item da lista multiplicando cada um por 3 e o 
# resultado é convertido em uma lista
print(
    list(map(
        lambda x: x * 3, 
        [1, 2, 3, 4, 5]
    ))
)
# output: [3, 6, 9, 12, 15]