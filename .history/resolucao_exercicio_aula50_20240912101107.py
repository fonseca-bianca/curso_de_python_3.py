"""Exercício:
exiba os índices da lista abaixo
"""

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista)) 
#len: percorre os valores da lista

print(indices)

for nome in lista:
    print(nome, type(nome))