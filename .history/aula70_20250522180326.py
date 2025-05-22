"""
Retorno de valores das funções (return).
SOMENTE de dentro da função, pq só função tem essa palavra
O retorno desses valores poderá ser utilizado no cód, seja em variáveis ou
outras partes do cód

print(): é uma função que só EXIBE coisas, valores na tela (saída do sistema)
NÃO tem valor (é None)
"""

def soma(x, y):
    return x + y
    # print(1 + 1) --> Code is unreachable

soma1 = soma(1, 1)
soma2 = soma(2, 2)

print(soma1 + soma2) 
# o código irá retornar a soma das duas variáveis soma1 e soma2, pq tem o 
# 'return' acima somando os valores de 'x' e 'y' 


# def soma(x, y):
#     print("Olha")
#     print("só")
#     print("que")
#     print("legal")
    
#     if x > 10:
#         return 10
#     return x + y # aq ´é como se fosse o 'else', mas NÃO precisa especificar, 
#                  # pq se a outra condição for FALSE, então o 2º return será 
#                  # lido
    
    

# soma1 = soma(1, 1)
# soma2 = soma(2, 2)

# print(soma1 + soma2) 


# Porque o código retorna "Olha só que legal" 2 vezes?
# Seria porque a frase "Olha só que legal" estaria nos lugares de 'x' e 'y'
# da função def soma???

# Retorno do código:
# Olha
# só
# que
# legal
# Olha
# só
# que
# legal
# 6

# --> O fluxo de execução é o seguinte:

#     Chama soma(1, 1): imprime "Olha", "só", "que", "legal", e 
# depois retorna 2.
#     Chama soma(2, 2): imprime "Olha", "só", "que", "legal", e 
# depois retorna 4.
#     Soma os resultados retornados (2 + 4 = 6) e imprime 6.
