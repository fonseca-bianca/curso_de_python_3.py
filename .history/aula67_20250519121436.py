""" 
Valores padrão para parâmetros:
ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor NÃO seja enviado pro Parâmetro, o valor padrão será usado

REFATORAR:
    editar o cód
"""

def soma(x, y, z=None): # enviados valores padrão dos parâmetros da função
    if z is not None: # se 'z' NÃO for None, usar o valor de 'z'
        print(f"{x=} {y=} {z=}", " | x + y + z =",  x + y + z)
    else: # se 'z' for None, NÃO usar o valor de 'z'
        print(f"{x=} {y=}", "| x + y + z =", x + y)
        
soma(1, 2) # 'z' recebe valor None
soma(100, 200) # 'z' recebe valor None
soma(7, 9 ,0) # bloco 'if' é executado pq 'z' recebe valor como parâmetro
        
    