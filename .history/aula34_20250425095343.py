"""
Repetições WHILE e BREAK:
while: executa ação enquanto for TRUE
*looping infinito: quando condição NÃO tem fim/pausa
break: para o bloco
"""

condicao = True

while condicao:
    nome = input("Digite o seu nome: ")
    print(f"\tO seu nome é {nome}")
    
    resposta = input("Digite 'sair' ou 's' pra fechar o programa: ")

    if resposta == "sair" or resposta == "s":
        break # esse 'break' busca o 'while' mais próximo dele

print("\tPrograma encerrado\n")

# se NÃO colocar esse Break aq, o programa vai pedir a mesma coisa 
# infinitamente, pois a condição estabelecida é True, ou seja, necessitaria 
# de uma condição seguinte False ou outra condição True ou se um Break pra 
# ocorrer sua interrupção







    