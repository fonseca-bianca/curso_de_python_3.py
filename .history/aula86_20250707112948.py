"""
Dictionary Comprehension e Set Comprehension:
"""

produto = {
    'nome': 'Notebook',
    'preco': 4500.00,
    'categoria': 'Eletrônico'
}

# for chave, valor in produto.items():
#     print(chave, valor)
    
dc = {
    chave: valor.upper() # Converte o valor para maiúsculas 
    if isinstance(valor, str) else valor 
    # onde for 'str', converte pra maiúsculas, onde não for, mantém o valor 
    # original
    for chave, valor
    in produto.items()
    if chave != 'categoria'  # Exclui a chave 'categoria'
}

print(dc)


# Exemplo de Dict Comprehension em uma Lista:
# lista de Tuplas
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

# Essa sintaxe percorre cada tupla na lista, desempacotando os elementos 
# como chave e valor. Constrói um dicionário
dc = {
    chave: valor
    for chave, valor in lista
}

print(dc)

