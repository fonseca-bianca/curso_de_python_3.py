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
    for chave, valor
    in produto.items()
}

print(dc)