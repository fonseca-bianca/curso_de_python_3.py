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
    chave: valor 
    for chave, valor
    in produto.items()
}
