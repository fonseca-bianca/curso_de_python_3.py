"""
Exercício: unindo listas

Crie uma função zipper (zipper de roupas) e ela deverá unir duas listas em 
ordem.
Use todos os valores da menor lista.
    ex.:
        ['Salvador', 'Ubatuba', 'Belo Horizonte']
        ['BA', 'SP', 'MG', 'RJ']
        
        # output:
        [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

def zipper(func):
    def wrapper(lista1, lista2):
        # aqui só estamos repassando o retorno
        return func(lista1, lista2)
    return wrapper

@zipper
def unir_listas(lista1, lista2):
    return list(zip(lista1, lista2))  # essa lógica será sobrescrita pelo decorador de cima

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(unir_listas(cidades, estados))
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]