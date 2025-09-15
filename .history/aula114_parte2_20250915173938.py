"""
Funções Recursivas e Recursividade:
"""

def factorial(n):
    # caso base/condição de parada:
    if n <= 1: 
        # Fatorial de 0! e 1! é sempre 1. Quando n chega a 1, a função 
        # para de chamar a si mesma e simplesmente retorna o valor 1
        return 1
    
    # parte recursiva:
    return n * factorial(n-1)

print(factorial(5))
print(factorial(10))