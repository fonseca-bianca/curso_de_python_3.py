x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return total
    
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)