"""Exercício:
exiba os índices da lista abaixo
"""

lista1 = ["Dragon-ball", "Cavaleiros do Zodíaco", "Pokémon"]
i = 0
lista1.append("HOTD")
i = range(len(lista1)) # range percorre os índices (valores) da lista
print(i)

for nome in lista1:
    print([i],":", nome, type(nome))
    i += 1 # incrementando a variável 'i' manualmente dentro do loop for pra 
    # atualizar o valor a cada iteração