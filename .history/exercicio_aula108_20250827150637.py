"""
Exercício: somando duas listas
Considerando duas listas de inteiros ou floats (lista A e lista B), SOME os
valores das listas retornando uma NOVA lista com os valores somados.
Se uma lista for maior do que a outra, a soma só vai considerar o tamanho da 
lista menor.

Ex.: 
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 7]
====================== RESULTADO:
lista_soma [5, 7, 9]
"""

def soma_listas(lista_a, lista_b):
    retorno = [
        a + b for a, b in zip(lista_a, lista_b)
    ]
    return retorno

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(soma_listas(lista_a, lista_b))