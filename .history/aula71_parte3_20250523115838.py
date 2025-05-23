"""
Função sum():
- soma todos os números de uma lista ou tupla
- é padrão do Python
- se usar ela, NÃO é necessário realizar o Desempacotamento, pq ela espera
um ÚNICO argumento (lista ou tupla) q seja iterável e não uma sequência de 
argumentos
ex.:
     sum(numeros) ✅ → Correto, porque sum() aceita iteráveis


Função personalizada soma():
- soma todos os números de uma lista ou tupla
- é uma função personalizada criada por nós mesmos
- se usar ela, é necessário realizar o Desempacotamento, pq ela espera
uma SEQUÊNCIA de argumentos (não uma lista ou tupla)
- ou seja, ela espera receber os números separados por vírgula e não uma lista 
ou tupla
ex.:
    soma(*numeros) ✅ → Correto, porque sua função personalizada espera 
        múltiplos argumentos

"""

def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return total
    
soma_peq = soma(1, 2, 3)
print(soma_peq)

# OU usar a função própria q o Python oferece q é a função sum():
print(sum((1, 2, 3))) 
#   a tupla deve ser copiada com os parênteses junto dentro do argumento 
# da função sum()

# OU outra forma de usar a função sum():
numeros = 1, 2, 3, 4, 5, 6, 7, 8 # tupla
usando_funcao_sum = soma(*numeros) # Desempacotamento da tupla 'numeros'


# Ambos os prints() abaixo retornam a soma dos números da tupla 'numeros'
print(usando_funcao_sum) 
# usa função soma() (q é personalizada, criada por nós mesmos
# def soma(*args):
#     total = 0 
#     for numero in args:
#         total += numero
#     return total)

print(sum(numeros)) # NÃO há Desempacotamento
# soma = sum(numeros) # usa a função sum() (q é padrão do Python)