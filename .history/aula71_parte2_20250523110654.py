"""
args - Argumentos NÃO nomeados
* - *args (desempacotamento)

"""
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
    
    

print("Outra forma de fazer a mesma coisa, mas usando o desempacotamento: ")


numeros = (1, 2, 3, 4, 5, 6)
def soma2(*args):
    total2 = 0
    for numero2 in args:
        print("Soma total anterior e total seguinte: ", total2, "+", numero2)
        total2 += numero2
        print("Total", total2)
        
    print(total2)
    
soma(*numeros) # desempacotamento