""" 
Introdução às Generator functions em Python:
ex.: generator = (n for n in range(100))

OBS.:
   - Generator function: 
        sabe PAUSAR a execução em determinado ponto e RETOMAR
        todo Generator é um Iterator, pq podemos chamar o 'next()' nele
a execução de onde parou 
   - Return: 
        PARA a execução da função e NÃO retorna mais nada
        OBS.: 
            pra PAUSAR, nesse caso, usamos o 'yield' e NÃO o 'return', pq
            'yield' pertence a Generator function

"""

def generator(n=0):
    yield 1 # pausar
    return 'acabaou' # não retorna mais nada, só para parar a execução

gen = generator(n=0)
print(gen)