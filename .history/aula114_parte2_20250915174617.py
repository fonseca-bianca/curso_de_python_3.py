"""
Funções Recursivas e Recursividade:

Esse print vai retornar um erro:
print(factorial(1000)) 

    [Previous line repeated 996 more times]
    RecursionError: maximum recursion depth exceeded:
        esse erro acontece pq, a Função Recursiva é uma PILHA de chamadas, ou
        seja, cada vez q a função se chama, ela é empilhada na CALL STACK.
        Python define um limite de segurança pra profundidade da recursão 
        pra evitar que a memória do computador se esgote (o que causaria um 
        erro fatal, normalmente vai até limite de 1000 chamadas recursivas).


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
# print(factorial(1000)) # [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded 
