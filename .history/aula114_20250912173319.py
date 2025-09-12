"""
Funções Recursivas e Recursividade:



* Se NÃO houver caso base de recursão (q é o caso q faz a parada), então a 
função recursiva vai chamar ela mesma infinitamente, até estourar a memória
e o interpretador do Python vai lançar um erro de 
RecursionError: maximum recursion depth exceeded
"""

def recursiva(inicio=0, fim=10):
    # caso base:
    if inicio >= fim:
        return fim
    print(inicio) # printa antes de chamar a função recursiva
    
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

