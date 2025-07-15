""" 
Introdução às Generator functions em Python:
ex.: generator = (n for n in range(100))

OBS.:
   - Generator function: 
        sabe PAUSAR a execução em determinado ponto e RETOMAR a execução 
de onde parou 
        todo Generator é um Iterator, pq podemos chamar o 'next()', 
'iter()' nele

   - Return: 
        PARA a execução da função e NÃO retorna mais nada
        OBS.: 
            pra PAUSAR, nesse caso, usamos o 'yield' e NÃO o 'return', pq
            'yield' pertence a Generator function

"""

# def generator(n=0):
#     yield 1 # PAUSA a execução e retorna o valor 1 e guarda o valor no next()
    
#     return 'acabaou' # não retorna mais nada pq PARA a execução

# gen = generator(n=0)
# print(gen)
# print(next(gen))
# print(gen.__iter__())

def generator(n=0):
    yield 1 # PAUSA 
    print("continuando a execução...")
    yield 2 # PAUSA
    
    
gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
