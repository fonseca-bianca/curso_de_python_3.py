""" 
Filtro (filter) de Dados em List Comprehensions:
    - depois do 'for' tem um 'if' e os itens podem ou não ser incluídos na 
    lista final
    - é uma função embutida (built-in) do Python
    - filtra elementos de uma sequência (lista, tupla, etc.) e mantém apenas
    os elementos q atendem a uma condição específica
    - Sintaxe:
        filter(function, iterable)
            function: vai retornar True ou False pra CADA item
            iterable: o objeto q está sendo filtrado (lista, tupla, etc.)
            RESULTADO:
                objeto do tipo filter
                pra ver o resultado, é necessário usar 'for' ou 'list()'
                
"""
# exemplo SEM função anônima (lambda):
def eh_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(eh_par, numeros)

print(list(pares))  # [2, 4, 6]
  
print()
        
# exemplo COM função anônima (lambda):
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)

print(list(pares))  # [2, 4, 6]