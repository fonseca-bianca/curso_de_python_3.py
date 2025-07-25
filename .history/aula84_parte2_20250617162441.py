"""
... continuação sobre List Comprehensions ...

Mapeamento de Dados em List Comprehensions:

"""

lista = [
    numero * 2 
    for numero in range(10)
]
print(list(range(10)))
print(lista)

# Mapeamento de Dados em List Comprehensions:
produtos = [
    {'nome': 'Produto 1', 'preco': 10.0},
    {'nome': 'Produto 2', 'preco': 20.0},
    {'nome': 'Produto 3', 'preco': 30.0},
]


# produtos_com_novo_valor = [
#     produto
#     for produto in produtos
# ]

# print(produtos_com_novo_valor) 
# se imprimir assim, fica igual e visualmente confuso
# output:
# [{'nome': 'Produto 1', 'preco': 10.0}, {'nome': 'Produto 2', 'preco': 20.0}, 
# {'nome': 'Produto 3', 'preco': 30.0}]


# Criando um NOVO dicionário com os valores (preço) atualizados conforme a 
# lógica:
produtos_com_novo_valor1 = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    # no NOVO dict estamos alterando a chave 'preco' do produto 
    for produto in produtos
]

print(*produtos_com_novo_valor1, sep='\n')

print()

produtos_com_novo_valor2 = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    # no NOVO dict estamos alterando a chave 'preco' do produto 
    if produto ['preco'] > 20 else {**produto} # retorna o produto inteiro
    for produto in produtos
]

print(*produtos_com_novo_valor2, sep='\n') 
# se usar o * (asterisco) na frente, desempacota a lista e usando o sep='\n',
# imprime cada dicionário em uma linha separada, fica mais organizado
