"""
args - Argumentos NÃO nomeados
* - *args (desempacotamento)
*kwargs - Argumentos nomeados
**kwargs - **kwargs (empacotamento)

"""
# Empacotamento (x, y) e Desempacotamento (*resto): 
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

print(soma(x, y)) # 3

# Retorno:
# 1 2 [3, 4] --> x = 1, y = 2, *resto = [3, 4]: o resto captura o restante 
# e empacota como uma lista, pois não será usado no cód
# 1
