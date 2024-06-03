#checar operador AND
entrada = input("[E] entrar | [S] saída: ")
senha_digitada = input("Insira a senha: ")

senha_permitida: 123456

#if = TRUE
if entrada == "[E]" and senha_digitada == senha_permitida:
    print("Entrada autorizada")
elif saida == "[S]" and senha_permitida:
    print("Saindo do sistema")
else:
    print("Acesso negado")
