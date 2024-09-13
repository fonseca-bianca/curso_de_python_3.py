"""Enumerate:
enumera valores de iteráveis (pegar índices)
enumerate é um ITERATOR --> por ser MAIS COMPLEXO, normalmente ele NÃO é colocado diretamente 
em uma variável, pq é como se criasse sempre um novo iterator, logo, os valores NUNCA se esgotariam
"""

lista1 = ["Dragon-ball", "Cavaleiros do Zodíaco", "Pokémon"]
lista1.append("HOTD")

lista_enumerada = list(enumerate(lista1))
print(lista_enumerada)
# enumera e retorna cada item da lista: [(0, 'Dragon-ball'), (1, 'Cavaleiros do Zodíaco'), (2, 'Pokémon'), (3, 'HOTD')]
# cada item da lista é retornado dentro de uma tupla ex.: (0, 'Dragon-ball')


# print(lista1)
# print(next(lista_enumerada), type(lista_enumerada)) # retorna: <enumerate object at 0x000002081D8B2A70>: núm do objeto lista na memória do programa


# para cada tupla, ele vai separar o indice e o desenho
for indice, desenho in lista_enumerada:
    print(indice, desenho) 
    # print(lista_enumerada) # mostra o objeto da lista na memória do programa <enumerate object at 0x000002BA86392980>

"""o for acima é o mesmo que:
for item in enumerate(lista1):
    indice, desenho = item
    print(indice, desenho)
"""    

"""q tbm é o mesmo que"""
for tupla_enumerada in enumerate(lista1):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'{valor}\t')
        
        # \t: em Python, é uma tabulação. Cria espaço horizontal pra melhor visualização dos itens