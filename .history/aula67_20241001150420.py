""" 
Valores padrão para parâmetros:
ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor NÃO seja enviado pro Parâmetro, o valor padrão será usado
"""

def soma(x, y, z=None):
    if z is not None: # se 'z' NÃO for None, usar o valor de 'z'
        print(f"{x=} {y=} {z=}", x + y + z)
    else: # se 'z' for None, NÃO usar o valor de 'z'
        print(f"{x=} {y=}", x + y)
        
soma(1, 2)
soma(100, 200)
soma(7, 9 ,0)
        
    