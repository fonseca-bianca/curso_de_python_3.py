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
    def inner(lista1, lista2): # inner (interna): criando decorador
        # wrapper (empacotador): convenção nome pra criar decorador
        return func(lista1, lista2)
    return inner

@zipper
def unir_listas(lista1, lista2):
    return list(zip(lista1, lista2))  
# zip: função nativa do Python combina 2 ou + listas/iteráveis:
# junta elementos correspondentes pelo índice em tuplas
# tuplas criadas: (lista1[0], lista2[0]), (lista1[1], lista2[1])...
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(unir_listas(cidades, estados))
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]