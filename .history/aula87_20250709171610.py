"""
isinstance:
    pra saber se o Objeto é de determinado tipo
    faz a checagem do tipo do objeto
"""

lista = [ 'a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Luiz'},
]


# for item in lista:
#     item.add(5) # TypeError: 'str' object has no attribute 'add'
#     # por isso, precisamos verifica o tipo com o 'isinstance' antes de
#     # chamar o .add() na variável 'item'
#     print(item)

# usando verificação com 'set' (vai trazer os métodos de 'set'):
for item in lista:
    if isinstance(item, set):
        item.add(5)  # Adiciona 5 ao conjunto se for do tipo set
        print(item, isinstance(item, set))
# OBS.:
# quando colocamos os parâmetros dentro do 'isinstance(item, set)', então 
# estamos dizendo pro programa que 'item' é um 'set', por isso o python permite 
# que chamemos o método '.add(5)' que é um método de 'set'


# usando verificação com 'str' (vai trazer os métodos de 'str'):
for item in lista:
    if isinstance(item, str):
        item.upper()  # aplica letra maiúscula onde houver 'str'
        print(item, isinstance(item, str))


# testando se mais de um tipo é 'set':
for item in lista:
    if isinstance(item, (set, list)):
        print(f'{item} é um set ou list')
