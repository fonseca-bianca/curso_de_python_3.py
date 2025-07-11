"""
Generator expression
Iterables
Iterators:
    entrega um valor por vez, pq ele só precisa saber o próximo valor
    -   __iter__()
    -   __next__()
"""

iterable = ["Eu", "tenho", "__iter__"]
iterator = iterable.__iter__() 