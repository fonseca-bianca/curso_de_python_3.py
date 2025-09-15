"""
Funções Recursivas e Recursividade:
- funções q podem se chamar de volta;
- úteis pra dividir problemas MAIORES em partes MENORES;
  * Toda função Recursiva terá:
    - Caso Base: condição de parada da recursão;
    - Caso Recursivo q resolve o PEQUENO problema;
    - um problema MAIOR q pode ser dividido em partes MENORES
    ex.: FATORIAL!
    5! = 5 * 4 * 3 * 2 * 1 = 120


* Se NÃO houver caso base de recursão (q é o caso q faz a parada), então a 
função recursiva vai chamar ela mesma infinitamente, até estourar a memória
e o interpretador do Python vai lançar um erro de 
RecursionError: maximum recursion depth exceeded
"""

def recursiva(inicio=0, fim=10):
    # caso base:
    # caso base vai ser chamado na última condição, no caso, no 10, ou seja,
    # Python vai na CALL STACK e desempilha as chamadas de função uma a uma
    
    if inicio >= fim:
        return fim
    print(inicio) # printa antes de chamar a função recursiva
    
    # print(inicio, fim)
    # 0 10
    # 1 10
    # 2 10
    # 3 10
    # 4 10
    # 5 10
    # 6 10
    # 7 10
    # 8 10
    # 9 10
    # 10

    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

