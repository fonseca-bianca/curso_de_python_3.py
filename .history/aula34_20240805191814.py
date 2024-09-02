"""
Repetições WHILE e BREAK:
while: executa ação enquanto for TRUE
*looping infinito: quando condição NÃO tem fim/pausa
break: para o bloco
"""

condicao = True

while condicao:
    nome = input("Digite o seu nome: ")
    print(f"O seu nome é {nome}")
    
    resposta = input("Digite 'sair' pra fechar o programa: ")
    if resposta == "sair":
        break 

print("Programa encerrado\n")
"""
se NÃO colocar esse Break aq, o programa vai pedir a mesma coisa infinitamente,
pois a condição estabelecida é True, ou seja, necessitaria de uma condição seguinte
False ou outra condição True ou se um Break pra ocorrer sua interrupção
"""

placar = 50
print(f"O placar é: {placar}")
    