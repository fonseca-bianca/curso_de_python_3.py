while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador desejado (+-*/): ")

    # Inicializar variáveis
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    # Bloco try...except para tratar exceções de conversão de números
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except ValueError:
        print("Um ou ambos números digitados são inválidos")
        continue

    # Verificar o operador
    operadores_permitidos = "+-*/"

    # verificar se o operador contém mais de um caractere
    if len(operador) > 1:
        print("Digite somente um operador por vez")
        # continue

    # verificar se o operador está na lista de operadores válidos
    elif operador not in operadores_permitidos:
        print("O operador digitado é inválido")
        # continue
    
    else:
        # O operador é válido e está na ordem correta
        print(f"Operador válido: {operador}")
        

    # Realizar a operação
    print("Operação realizada. Confira o resultado: ")
    if operador == "+":
        print(f"{num_1_float} + {num_2_float} = {num_1_float + num_2_float}")
    elif operador == "-":
        print(f"{num_1_float} - {num_2_float} = {num_1_float - num_2_float}")
    elif operador == "*":
        print(f"{num_1_float} * {num_2_float} = {num_1_float * num_2_float}")
    elif operador == "/":
        if num_2_float == 0:
            print("Não é possível dividir por zero")
        else:
            print(f"{num_1_float} / {num_2_float} = {num_1_float / num_2_float}")

    # Perguntar se deseja sair
    sair = input("Deseja sair? [s] / [n]: ").strip().lower()
    if sair.startswith("s"):
        break