"""
args - Argumentos NÃO nomeados
* - *args (empacotamento e desempacotamento)

"""
# Desempacotamento:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    print(args)
    
print(1, 2, 3, 4, 5, 6)
    
