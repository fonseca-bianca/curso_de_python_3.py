"""Jogo palavra secreta
Usuário deverá adivinhar a palavra
1) usuário poderá digitar apenas 1 letra;
2) após, o programa deverá conferir se a letra digitada está dentro da palavra secreta;
3) se estiver, o programa deverá exibir a letra;
4) se não estiver, o programa deverá exibir "*";
5) faça a contagem de tentativas que o usuário tentou.
"""

palavra_secreta: "tecnologia"

for letra in range(26): # percorre de 0 a 9
    if i == 2:
        print("i é 2, pulando...")
        continue
    
    if i == 8:
        print("i é 8, seu else não executará se houver um 'break' no código")
        continue
    
    for j in range(1, 3): #para cada valor de i (exceto quando i == 2), este loop aninhado percorre os valores de j de 1 até 2, imprimindo o par (i, j) 
        #range inclui o valor final 3, mas NÃO vai até ele
        print(i, j) #linha, coluna
        
else:
    print("Loop 'for' completado com sucesso")

