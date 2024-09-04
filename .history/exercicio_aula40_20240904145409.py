while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador desejado (+, -, *, /): ")
    
    numeros_validos = None #criando uma flag (bandeira) de aviso
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos números digitados são inválidos")
        continue
    
    sair = input("Deseja sair? [s] / [n]").lower().startswith("s")
    
    if sair is True:
        break
    
    # try:
    #     ...
    # except Exception as error: 
    #   # variável do erro 'error' --> para saber qual erro: print(error)
    #     ...