"""
Operadores Lógicos:
    and (e): TODAS condições precisam ser verdadeiras
    or (ou): APENAS uma condição precisa ser verdadeira
    not (não): inverte o valor lógico da condição
"""

#checar operador AND
entrada = input("[E] entrar ou [S] sair? ")

senha_permitida = '123456'

#if = TRUE
if entrada.lower() == "e":
    senha_digitada = input("Insira a senha: ")
    if senha_digitada == senha_permitida:
        print("Entrada autorizada")
    else:
        print("Acesso negado")
elif entrada.lower() == "s":
    print("Saindo do sistema")
else:
    print("Opção inválida")
    
