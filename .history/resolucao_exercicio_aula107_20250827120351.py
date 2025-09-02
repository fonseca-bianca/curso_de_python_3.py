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

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2)) # pega o tamanho da menor lista
    return [
        (l1[i], l2[i]) for i in range(intervalo)
    ]
    
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

print("-------------------------------------------------------------------")

# outra forma de escrever, agora considerando seguir a lista MAIOR usando o 
# pacote 'zip_longest':
# https://docs.python.org/3/library/itertools.html#itertools.zip_longest
# itertools.zip_longest(*iterables, fillvalue=None) --> sintaxe pra chamar
# zip_longest que é uma função da biblioteca itertools.
# neste caso, zip_longest está SEM parênteses pq é a REFERÊNCIA pra função

from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(lista_1, lista_2)))
print(list(zip_longest(lista_1, lista_2, fillvalue = "SEM Cidade")))