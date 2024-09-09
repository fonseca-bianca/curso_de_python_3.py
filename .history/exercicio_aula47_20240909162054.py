"""Jogo palavra secreta
Usuário deverá adivinhar a palavra
1) usuário poderá digitar apenas 1 letra;
2) após, o programa deverá conferir se a letra digitada está dentro da palavra secreta;
3) se estiver, o programa deverá exibir a letra;
4) se não estiver, o programa deverá exibir "*";
5) faça a contagem de tentativas que o usuário tentou.
"""

import os

palavra_secreta = "tecnologia"
letras_corretas = "" 
# letras corretas vão ser salvas dentro da string vazia 'letras_corretas'
numero_tentativas = 0

while True: 
    letra_digitada = input("Digite uma letra de A a Z: ")
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print("Digite somente uma letra")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    else:
        print(f"A letra '{letra_digitada}' não está na palavra secreta")
    
    palavra_formada = "" # criada DENTRO do while
    # a cada execução do 'while', o 'for' irá fazer a conferência se a letra estiver na palvra secreta, então o programa vai exibir a letra. Essa letra será mantida
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
           palavra_formada += letra_secreta 
            # print(letra_secreta) --> se esse print ficasse, então a palavra ficaria na vertical
        # se a letra digitada não estiver na palavra secreta, então o programa vai exibir um '*'
        else:
            palavra_formada += "*"
            # print("*") --> se esse print ficasse, então a palavra ficaria na vertical
    
    print(f"Palavra formada: {palavra_formada}") # print fora do 'for'
    
    if palavra_formada == palavra_secreta:
        os.system("clear") # limpando o terminal ANTES de o usuário ganhar
        print(f"Parabéns! Você acertou! A palavra secreta é: {palavra_secreta}")
        print(f"O número de tentativas foi: {numero_tentativas}")
        
        # pro programa retornar para ZERO quando o usuário acertar a palavra.
        # aí o jogo irá recomeçar
        letras_corretas = "" 
        numero_tentativas = 0
        

    
    
    
    
   

