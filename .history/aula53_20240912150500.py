"""Enumerate:
enumera valores de iteráveis (pegar índices)
"""

lista1 = ["Dragon-ball", "Cavaleiros do Zodíaco", "Pokémon"]
lista1.append("HOTD")

lista_enumerada = enumerate(lista1)
print(lista1)
print(next(lista_enumerada), type(lista_enumerada)) # retorna: <enumerate object at 0x000002081D8B2A70>: núm do objeto lista na memória do programa

for item in lista_enumerada:
    print(item) 
    print(lista_enumerada)