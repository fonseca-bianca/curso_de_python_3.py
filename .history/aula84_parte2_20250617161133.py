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


produtos_com_novo_valor = [
    produto
    for produto in produtos
]

print(produtos_com_novo_valor) 
# se imprimir assim, fica igual e visualmente confuso

print()

print(*produtos_com_novo_valor, sep='\n') 
# se usar o * (asterisco) na frente, desempacota a lista e usando o sep='\n',
# imprime cada dicionário em uma linha separada, fica mais organizado
