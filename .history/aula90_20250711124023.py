"""
Generator expression
Iterables
Iterators:
    entrega um valor por vez, pq ele só precisa saber o próximo valor
    esgota os valores (se tem 3 valores, ele entrega o 1º, depois o 2º,
depois o 3º, e depois não tem mais nada)
    -   __iter__()
    -   __next__()
"""

iterable = ["Eu", "tenho", "__iter__"]
iterator = iterable.__iter__() 