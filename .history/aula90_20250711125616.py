"""
Generator expression:
    funções q sabem pausar em determinada condição, por isso, usada DIRETO
Iterables
Iterators:
    entrega um valor por vez, pq ele só precisa saber o próximo valor
    esgota os valores (se tem 3 valores, ele entrega o 1º, depois o 2º,
depois o 3º, e depois não tem mais nada)
    pode convertê-lo em uma lista, tupla, etc. se quiser
    -   __iter__()
    -   __next__()
    normalmente trabalha com o iterable, que é o objeto que tem
    __iter__() e __next__()
    NÃO usa direto, tem q ter o iterável e o iterador
"""

iterable = ["Eu", "tenho", "__iter__"]
iterator = iter(iterable) 
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration Error, pq só tem 3 valores


# Generator expression:
generator = (x for x in range(3))  # parece uma Tupla, mas NÃO é
print(generator)