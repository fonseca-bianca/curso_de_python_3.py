"""Exercício:
exiba os índices da lista abaixo
"""

lista1 = ["Dragon-ball", "Cavaleiros do Zodíaco", "Pokémon"]
i = 0
indice = range(len(lista1)) # range percorre os índices (valores) da lista
print(indice)

for nome in lista1:
    print(nome, [i])
    i += 1 # incrementando a variável 'i' manualmente dentro do loop for pra atualizar o valor a cada iteração