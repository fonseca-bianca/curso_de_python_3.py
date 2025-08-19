"""
1) Aumente os preços dos produtos a seguir em 10%.
   Gere novos_produtos por deep copy (cópia profunda)
2) Ordene os produtos por nome em ordem Decrescente.
   Gere produtos_ordenados_por_nome por deep copy
3) Ordene os produtos por preço Crescente
   Gere produtos_ordenados_por_preco por deep copy
"""

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = []
print(novos_produtos.sorted())