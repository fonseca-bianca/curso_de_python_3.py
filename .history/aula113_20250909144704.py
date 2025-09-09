"""
Reduce: reduz um iterável em um único valor
"""
from functools import reduce
# No Python 3, foi movido para functools, pq em geral o uso de loops ou 
# list comprehensions é mais legível

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]