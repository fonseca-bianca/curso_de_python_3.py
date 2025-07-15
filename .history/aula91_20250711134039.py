""" 
Introdução às Generator functions em Python:
ex.: generator = (n for n in range(100))

OBS.:
   - Generator function: 
        sabe PAUSAR a execução em determinado ponto e RETOMAR
a execução de onde parou 
   - Return: 
        PARA a execução da função e NÃO retorna mais nada

"""

def generator(n=0):
    return 1

gen = generator(n=0)
print(gen)