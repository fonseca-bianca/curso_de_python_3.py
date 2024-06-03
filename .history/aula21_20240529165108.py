#checar operador AND
entrada = input("[E] entrar | [S] saída: ")
senha_digitada = input("Insira a senha: ")

senha_permitida: 123456

#if = TRUE
if entrada == "[E]" and senha_digitada == senha_permitida:
    print("Entrada autorizada")
else:
    print("Acesso negado")
