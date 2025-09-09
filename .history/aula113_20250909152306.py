"""
Reduce: reduz um iterável em um único valor
- precisa de um acumulador (armazena o valor parcial)
- função recebe 2 parâmetros: o acumulador e o item atual do iterável (q está 
iterando)
- o ACUMULADOR é o iterável
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

# Abaixo temos o Acumulador (soma_total) e o item atual (produto)
# soma_total = 0
# for produto in produtos:
#     soma_total += produto['preco']
    
# print(f"{soma_total:.2f}")

# ou assim:
# print(sum([produto['preco'] for produto in produtos]))


# com Reduce:

def funcao_do_reduce(acumulador, produto): # acumulador e o item iterável
    print(f"Acumulador: {acumulador}")
    print(f"Produto atual: {produto}")
    print()
    return acumulador + produto['preco'] # lista de preço []

soma_total = reduce(
    funcao_do_reduce,
    produtos,
    0 # esse é o valor inicial
)

print(f"A soma total de todos os acumuladores é: {soma_total:.2f}")