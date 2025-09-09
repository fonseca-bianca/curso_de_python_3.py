""" 
Filter - é um filtro funcional
"""

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]
print("Todos os produtos:")
print(*produtos, sep='\n')

print("\nProdutos com preço maior que 10:")
print(*novos_produtos, sep='\n')