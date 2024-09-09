"""Jogo palavra secreta
Usuário deverá adivinhar a palavra
1) usuário poderá digitar apenas 1 letra;
2) após, o programa deverá conferir se a letra digitada está dentro da palavra secreta;
3) se estiver, o programa deverá exibir a letra;
4) se não estiver, o programa deverá exibir "*";
5) faça a contagem de tentativas que o usuário tentou.
"""

palavra_secreta = "tecnologia"
letras_corretas = "" # letras corretas vão ser salvas dentro de uma string vazia

while True:
    letra_digitada = input("Digite uma letra de A a Z: ")
    
    if len(letra_digitada) > 1:
        print("Digite somente uma letra")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    else:
        print("A letra não está na palavra secreta")
        

    print(letras_corretas)
    
    
    
    # letra in alfabeto: # percorre de A a Z
    # if letra == a:
    #         print("a letra está na palavra")
    #         continue
    # else:
    #     print("a letra não está na palavra")
    
    
   

