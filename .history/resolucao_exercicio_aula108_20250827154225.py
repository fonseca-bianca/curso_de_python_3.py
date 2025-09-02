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

# Solução mais Genérica que NÃO utiliza os recursos nativos do Python, isto é,
# funcionaria em qlqr LP:

# _ : é o mesmo q dizer "NÃO queremos o valor, apenas o índice correspondente
# ex.: índice 0 = 1, então, pegue só o 1 pra fazer a soma"


print("Solução 1: Genérica, lida em qlqr LP:")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


print("Solução 2: mais 'Pythonica' usando 'enumerate':")

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


print("Solução 3: mais 'Pythonica' usando 'list comprehension' (ver minha):")

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(list(zip(lista_a, lista_b))) # [(1, 1), (2, 2), (3, 3), (4, 4)]
print(lista_soma)