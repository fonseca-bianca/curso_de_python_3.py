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
import sys

iterable = ["Eu", "tenho", "__iter__"]
iterator = iter(iterable) 
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration Error, pq só tem 3 valores


# Lista Comprehension:
lista = [x for x in range(10)]  # é uma List Comprehension
print(sys.getsizeof(lista)) # mostra qtd de Bytes que ocupa na memória

# vantagem da Lista:
# podemos acessar os valores pelos índices, como lista[0], lista[1] etc., 
# podemos saber o tamanho da lista
# isso NÃO ocorre com o Generator Expression


# Generator expression:
generator = (x for x in range(10))  # parece uma Tupla, mas NÃO é
print(sys.getsizeof(generator)) # mostra qtd de Bytes que ocupa na memória
print(next(generator))  # entrega o primeiro valor
print(next(generator))  # entrega o segundo valor                                   
print(next(generator))  # entrega o terceiro valor
# e assim sucessivamente, até esgotar os valores

# output: <generator object <genexpr> at 0x0000027D91744A00>
# existe uma Generator Expression nesse local da memória

# OBS.:
# Iterável com Iterator:
#   Salva TODOS os valores na memória
#   à medida que o valor do range() aumenta, o Python vai salvando
#   todos os valores na memória, ocupando mais espaço
# Generator Expression:
#   entrega um valor por vez e NÃO salva todos os valores na memória
#   à medida que o valor do range() aumenta, o Python NÃO salva
#   todos os valores na memória, ocupando menos espaço