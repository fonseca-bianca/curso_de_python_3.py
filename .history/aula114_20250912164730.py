"""
Funções Recursivas e Recursividade:

"""

def recursiva(inicio=0, fim=10):
    inicio += 1
    return recursiva(inicio, fim)

recursiva()

