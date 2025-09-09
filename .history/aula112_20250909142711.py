""" 
Filter - é um filtro funcional:
  - no exemplo abaixo, colocamos uma condição pra filtrar os produtos, logo,
    apenas os produtos com preço maior que 10 serão retornados na nova lista
    'novos_produtos'
  - o filter retorna um objeto iterável (filter object), logo, é necessário
    converter esse objeto em uma lista (list()) ou tupla (tuple()) ou set 
    (set())  
    

"""

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# usando List Comprehension:
novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]
print("Todos os produtos:")
print(*produtos, sep='\n') 
# tem q desempacotar a lista pra imprimir cada item de cada dict numa linha

print("\nProdutos com preço maior que 10:")
print(*novos_produtos, sep='\n')


print("--------------------------------------------------------------------")

# usando Filter:
novos_produtos_2 = filter(
    lambda p: p['preco'] > 20,
    produtos
)

# 1º parâmetro é uma função (lambda)
# 2º parâmetro é um iterável (lista, tupla, set, dict, str)