def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return total
    
soma_peq = soma(1, 2, 3)
print(soma_peq)