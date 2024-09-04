## Calculadora com 4 operadores matemáticos ##
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador desejado (+-*/): ")
    
    # declarar "num_1_float" e "num_2_float" fora do escopo do bloco try...except pra não ter erro no cód a posteriori
    numeros_validos = None # criando uma flag (bandeira) de aviso
    num_1_float = 0
    num_2_float = 0
    
    # bloco try...except pra tratar exceções quando o usuário digitar algo inválido pra leitura do programa
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos números digitados são inválidos")
        continue
    
    ##########################################################
    operadores_permitidos = "+-*/"
    
    if operador not in operadores_permitidos:
        print("O operador digitado é inválido")
        continue
    
    if len(operador) > 1 :
        print("Digite somente um operador por vez")
        continue
    
    ##########################################################
    print("Operação realizada. Confira o resultado: ")
    if operador == "+":
        print(f"{num_1_float} + {num_2_float} = ", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float} - {num_2_float} = ", num_1_float - num_2_float)
    elif operador == "*":
        print(f"{num_1_float} * {num_2_float} = ", num_1_float * num_2_float)
    elif operador == "/":
        print(f"{num_1_float} / {num_2_float} = ", num_1_float / num_2_float)
    else:
        print("O programa deveria chegar aqui")
    
    sair = input("Deseja sair? [s] / [n]: ").lower().startswith("s")
    
    if sair is True:
        break
    
    # try:
    #     ...
    # except Exception as error: 
    #   # variável do erro 'error' --> para saber qual erro: print(error)
    #     ...