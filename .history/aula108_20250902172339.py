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
    
    * range(): NÃO é um iterator
    
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
      se chamarmos o 'iter' do iterator, ele chama o próprio iterator
"""

from itertools import count

c1 = count()
r1 = range(10)

print(next(c1)) # entrega o valor inicial q é 0
print(next(c1)) # soma +1 e mostra 1