"""
isinstance:
    pra saber se o Objeto é de determinado tipo
    faz a checagem do tipo do objeto
"""

lista = [ 'a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Luiz'},
]

for item in lista:
    item.add(5)
    print(item)
