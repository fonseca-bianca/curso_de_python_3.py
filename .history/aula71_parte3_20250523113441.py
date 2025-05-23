# def soma(*args):
#     total = 0 
#     for numero in args:
#         total += numero
#     return total
    
# soma_peq = soma(1, 2, 3)
# print(soma_peq)

# # OU usar a função própria q o Python oferece q é a função sum():
# print(sum((1, 2, 3))) 
#   a tupla deve ser copiada com os parênteses junto dentro do argumento 
# da função sum()

# OU outra forma de usar a função sum():
numeros = 1, 2, 3, 4, 5, 6, 7, 8 # tupla
usando_funcao_sum = soma(*numeros) # Desempacotamento da tupla 'numeros'

print(usando_funcao_sum)
# soma = sum(numeros) 
print(sum(numeros)) # NÃO há Desempacotamento