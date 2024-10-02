"""
args - Argumentos NÃO nomeados
* - *args (empacotamento e desempacotamento)

"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

print(1)