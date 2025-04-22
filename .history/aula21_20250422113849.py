"""
Operadores Lógicos:
    * and (e): TODAS condições precisam ser verdadeiras
    * or (ou): APENAS uma condição precisa ser verdadeira
    * not (não): inverte o valor lógico da condição
    * in: verifica se o valor está dentro de uma lista ou string
    * is: verifica se o valor é do mesmo tipo
    * is not: verifica se o valor NÃO é do mesmo tipo
    **OBS.:
        - Se QLQR valor for considerado FALSO, a expressão ineira será FALSA
        - São considerados 'falsy':
            * 0, 0.0
            * "", '', [], (), {}
            * None: representa um NÃO valor
            * False
"""

# checar operador AND: pq estamos verificando 'entrada' e 'senha_digitada'
# ao mesmo tempo

entrada = input("[E] entrar ou [S] sair? ") 
senha_permitida = '123456' # como se estivesse puxando de um BD

# if condicao (TRUE): 
# ...

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
    
