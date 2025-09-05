"""
Combinations, Permutations e Product - itertools

* Combinations:
    Retorna todas as combinações possíveis de um iterável, sem repetição.
    ordem NÃO importa
    recebe:
        iterável + tamanho da combinação
    Ex.: combinations([1, 2, 3], 2) -> (1, 2), (1, 3), (2, 3)
    

** Permutations:
    Retorna todas as permutações possíveis de um iterável, com repetição.
    ordem IMPORTA
    recebe:
        iterável + tamanho da permutação
    Ex.: permutations([1, 2, 3], 2) 
    -> (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

*** Product:
    Retorna o produto cartesiano de dois ou mais iteráveis.
    ordem IMPORTA e REPETE valores únicos
    recebe:
        iteráveis
    Ex.: product([1, 2], [3, 4]) -> (1, 3), (1, 4), (2, 3), (2, 4)

** Itertools **: 
    é módulo padrão do Python e alberga várias funções q criam
    iteradores de forma mais eficiente no código
"""