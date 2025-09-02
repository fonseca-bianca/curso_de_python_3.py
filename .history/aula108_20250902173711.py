"""
count(): 
    conta quantas vezes um elemento aparece em uma lista infinitamente
    (serve pra quando NÃO sabemos o número de iterações)
    NÃO é nativo do Python:
        está no itertools (módulo), e count é uma função dentro dele
        
        Chamada:
        from itertools import count
    
    como ele é um iterator então, sempre q for chamado um next(), ele vai ser
    iterado +1 e retornar o valor atualizado
    
    * range(): NÃO é um iterator, MAS é iterável
    
        Range      |      Count
    -------------- | ----------------
    __iter__       | __len__
    __next__       | __getitem__
    melhor qndo    | continua gerando 
    sabemos número | números até ser 
    de iterações,  | explicitamente 
    pq ele tem um  | interrompido por
    limite         | um 'break'
    
    OBS.:
      se chamarmos o 'iter' em um iterator, ele retorna o próprio iterador
"""

from itertools import count

c1 = count()
r1 = range(10)

print(next(c1)) # entrega o valor inicial q é 0
print(next(c1)) # soma +1 e mostra 1

# c1 é um iterator:
print("c1", hasattr(c1, "__iter__")) # True pq tem o método __iter__
print("c1", hasattr(c1, "__next__")) # True pq tem o método __next__

# r1 NÃO é um iterador, MAS é um iterável:

print("r1", hasattr(r1, "__iter__")) # True pq tem o método __iter__
print("r1", hasattr(r1, "__next__")) # False pq NÃO tem o método __next__

for i in c1:
    if i >= 100:
        break
    
    print(i)