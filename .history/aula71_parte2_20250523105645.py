"""
args - Argumentos NÃO nomeados
* - *args (desempacotamento)

"""
# Desempacotamento:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0 # acumulação: soma ele mesmo mais o valor que está sendo passado
    for numero in args:
        print("Soma total anterior e total seguinte: ", total, "+", numero)
        total += numero
        print("Total", total)
    print(total)
    
    
    # args = list(args) # converte tupla args pra lista (MUTÁVEL) e está pode 
    # ser alterada
    # print(args, type(args)) # é uma tupla (IMUTÁVEL)
    
soma(1, 2, 3, 4, 5, 6)
    
    

