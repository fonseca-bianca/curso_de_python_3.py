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

# var 'produtos_valor_triplicado' recebe o resultado da função map e converte
# em uma lista
# map vai retornar objeto iterável e o list materializa esse objeto em uma
# lista
# lambda p: é o nome da função anônima
# 'p': é o dict atual
# na linha da função lambda é onde está a criação do NOVO dicionário
# **p: desempacotamento de todas key-value do dict 'p' do dict atual e os 
# insere no NOVO dict criado
# 'preco': p['preco'] * 3: sobrescreve a key 'preco' e acessa o preço do 
# produto original (p['preco']) e multiplica por 3 e atribui o novo valor à 
# key 'preco' no novo dicionário.

produtos_valor_triplicado = list(map(
    lambda p: {**p, 'preco': p['preco'] * 3},
    produtos
))


# uso do 'for' pq há uma LIST com vários DICT
# for:
#   em cada "volta" do loop, ele pega um dicionário completo e o atribui à
#   var 'produto'
# Processa CADA um dos dicionários da lista 'produtos'
# OBS.: 
#   se NÃO houvesse vários dicionários, poderia acessar o item da lista 
#   pelo índice correspondente


for produto in produtos:
    print(f"{produto['nome']} com valor original: R${produto['preco']}")

print()  
for produto in produtos_valor_triplicado:
    print(
        f"{produto['nome']} com valor triplicado: "
        f"R${produto['preco']:.2f}"
    )