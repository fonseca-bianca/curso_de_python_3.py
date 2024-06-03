#checar operador AND
entrada = input("[E] entrar ou [S] sair? ")
senha_digitada = input("Insira a senha: ")

senha_permitida: 123456

#if = TRUE
if entrada == "[E]" and senha_digitada == senha_permitida:
    print("Entrada autorizada")
elif entrada == "[S]" and senha_digitada == senha_permitida:
    print("Saindo do sistema")
else:
    print("Acesso negado")
