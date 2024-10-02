"""
args - Argumentos NÃO nomeados
* - *args (empacotamento e desempacotamento)

"""
# Desempacotamento:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    # args = list(args) # converte tupla args pra lista (MUTÁVEL) e está pode ser alterada
    print(args, type(args)) # é uma tupla (IMUTÁVEL)
    
soma(1, 2, 3, 4, 5, 6)
    
