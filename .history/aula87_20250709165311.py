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


for item in lista:
    if isinstance(item, set):
        item.add()
        print(item, isinstance(item, set))
