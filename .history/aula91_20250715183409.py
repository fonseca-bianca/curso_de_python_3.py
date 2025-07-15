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
    
#     return 'acabou' # não retorna mais nada pq PARA a execução

# gen = generator(n=0)
# print(gen)
# print(next(gen))
# print(gen.__iter__())

def generator(n=0):
    yield n # PAUSA 
    print("continuando a execução...")
    yield n + 1 # PAUSA
    print("continuando a execução...")
    yield n + 2 # PAUSA
    print("o programa termina aqui")
    return "acabou" # PARA a execução. Vai aparecer dentro do StopIteration


# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen)) 
# print(next(gen)) 
# # print(next(gen)) # StopIteration: é uma EXCEÇÃO q pode ser tratada com 'for'

# tratando o StopIteration com 'for':
gen = generator(n=0)
for n in gen:
    print(n)
    

print()    
# usando While True para tratar o StopIteration:
def generator_2(n=0, maximum=10): # função generator_2 criada 
# função inicia em 0 e vai até 10
    while True: # laço infinito
        yield n # PAUSA e entrega o valor atual de n
        n +=1   # incrementa 'n' em 1 até chegar no máximo q é 10
        
        if n > maximum: # se passar do limite q é 10
            return "Acabou a execução" # então o generator será encerrado

gen_2 = generator_2(maximum=20) # generator_2 é criado e recebe a função gerador SEM 
# parâmetros (MAS podemos colocar um maximum maior aqui, ex.: maximum=20)
for n in gen_2: # laço 'for' pra iterar sobre a função 'generator_2'
    print(n)    # imprime o valor de 'n' a cada iteração até chegar no máximo
