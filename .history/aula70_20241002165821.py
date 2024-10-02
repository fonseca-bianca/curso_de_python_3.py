"""
Retorno de valores das funções (return).
SOMENTE de dentro da função, pq só função tem essa palavra
O retorno desses valores poderá ser utilizado no cód, seja em variáveis ou outras
partes do cód

print(): é uma função que só EXIBE coisas, valores na tela (saída do sistema)
NÃO tem valor (é None)
"""

def soma(x, y):
    return x + y
    print(1 + 1)

soma1 = soma(1, 1)
soma2 = soma(2, 2)

print(soma1 + soma2) 
""" o código irá retornar a soma das duas variáveis soma1 e soma2, pq tem o 'return'
acima somando os valores de 'x' e 'y' """
