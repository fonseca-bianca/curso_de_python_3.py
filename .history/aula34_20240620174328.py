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

print("Programa encerrado")
"""
se NÃO colocar esse Break aq, o programa vai pedir a mesma coisa infinitamente,
pois a condição estabelecida é True, ou seja, necessitaria de uma condição seguinte
False ou outra condição True ou se um Break pra ocorrer sua interrupção
"""

contador = 0

while contador < 10:
    print(contador) #vem ANTES do 'contador' ser incrementado e mostra o valor inicial do contador
    contador = contador + 1
    # print(contador): se vier DEPOIS do 'contador', então será primeiro incrementado pra depois ser impresso
    
print("Acabou a contagem.")
    