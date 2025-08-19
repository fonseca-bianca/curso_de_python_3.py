"""
1) Aumente os preços dos produtos a seguir em 10%.
   Gere novos_produtos por deep copy (cópia profunda)
2) Ordene os produtos por nome em ordem Decrescente.
   Gere produtos_ordenados_por_nome por deep copy
3) Ordene os produtos por preço Crescente
   Gere produtos_ordenados_por_preco por deep copy
"""

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print("1) Produtos com aumento de 10%:")
novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] *= 1.1 # A lógica é: 1 + (percentual / 100)
print(f"Novos produtos com aumento de 10%: ")
for produto in novos_produtos:
    print(f"{produto['nome']} R${produto['preco']:.2f}")
    # :.2f só funciona para números (float/int), por isso tem q ser separado
    # pq ele não funciona na lista inteira


# OBS.: pq usar key e value no .sort()?
#   .sort(reverse=True) sem key tenta ordenar a lista inteira de dict 
# comparando os dicit entre si.
# Em Python, dict não têm uma ordem natural de comparação, então a ordenação 
# pode não sair como esperado, portanto, usar key + value


print("2) Produtos ordenados por nome (Decrescente):")

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(
    key=lambda nome_produto: nome_produto['nome'], reverse=True
    )
print(produtos_ordenados_por_nome)
# 'nome' (entre aspas) é a chave do dicionário
# nome_produto['nome'] é a operação que acessa essa chave para obter o 
# seu valor (que no exemplo é a str 'Produto 1', 'Produto 2', etc.)


print("3) Produtos ordenados por preço (Crescente):")

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(
    key=lambda produto: produto['preco'], reverse=False
    )
print(produtos_ordenados_por_preco)