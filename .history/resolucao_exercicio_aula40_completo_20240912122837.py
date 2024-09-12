# Lista dos operadores permitidos na ordem especificada
operadores_validos = "+-*/"
 
# Verifica se o operador contém mais de um caractere
if len(operador) > 1:
    print("Digite somente um operador por vez")
# Verifica se o operador está na lista dos operadores válidos
elif operador not in operadores_validos:
    print("Operador inválido")
else:
    # O operador é válido e está na ordem correta
    print(f'Operador aceito: {operador}')