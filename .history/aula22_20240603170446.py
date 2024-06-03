#Operador Lógico OR
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = 123

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")
    
# colocando entre parênteses a expressão q quer q seja lida primeiro, o programa
# vai ler ela pra depois verificar, se necessário, a outra expressão

senha = input("Senha: ") or "Sem senha"
print(senha)