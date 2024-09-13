"""Enumerate:
enumera valores de iteráveis (pegar índices)
enumerate é um ITERATOR --> por ser MAIS COMPLEXO, normalmente ele NÃO é colocado diretamente 
em uma variável, pq é como se criasse sempre um novo iterator, logo, os valores NUNCA se esgotariam
"""

lista1 = ["Dragon-ball", "Cavaleiros do Zodíaco", "Pokémon"]
lista1.append("HOTD")

lista_enumerada = enumerate(lista1)
# print(lista1)
# print(next(lista_enumerada), type(lista_enumerada)) # retorna: <enumerate object at 0x000002081D8B2A70>: núm do objeto lista na memória do programa

for item in lista_enumerada:
    print(item) 
    # print(lista_enumerada) # mostra o objeto da lista na memória do programa <enumerate object at 0x000002BA86392980>