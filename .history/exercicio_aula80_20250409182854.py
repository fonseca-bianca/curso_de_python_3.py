"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
        Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
    
    
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

"""Resolução do exercício:"""

def encontra_primeiro_duplicado(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    # função: vai retornar o primeiro número que aparece repetido (ou seja, a primeira duplicação 
    # encontrada ao percorrer a lista). 
    #         -1 se não houver duplicados.
    # set(): é um conjunto vazio q vai armazenar os números já checados.
    # primeiro_duplicado: variável que vai armazenar o primeiro número duplicado encontrado. 
    #                    -1 é o valor padrão, caso não haja duplicados.
    
    for numero in lista_inteiros: # vai percorrer cada número da lista de inteiros
        if numero in numeros_checados: # verificar a duplicação. Se o número atual já estiver no conjunto set() de numeros_checados, então ele será considerado como duplicado
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)
        
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )