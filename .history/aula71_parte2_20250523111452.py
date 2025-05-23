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


numeros = (1, 2, 3, 4, 5, 6) # declarada a tupla antes da função
def soma_b(*args):
    total_b = 0
    for numero_b in args:
        print("Soma total anterior e total seguinte: ", total_b, "+", numero_b)
        total_b += numero_b # total2 = total2 + numero2
        print("Total", total_b)
        
    print(total_b)
    
soma_b(*numeros) # desempacotamento