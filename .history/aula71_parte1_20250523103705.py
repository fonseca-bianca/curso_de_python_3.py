"""
args - Argumentos NÃO nomeados
* - *args (empacotamento e desempacotamento)

"""
# Desempacotamento:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

print(soma(x, y))

# Retorno:
# 1 2 [3, 4] --> x = 1, y = 2, *resto = [3, 4]: o resto captura o restante 
# e empacota como uma lista, pois não será usado no cód
# 1
