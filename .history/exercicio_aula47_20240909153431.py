"""Jogo palavra secreta
Usuário deverá adivinhar a palavra
1) usuário poderá digitar apenas 1 letra;
2) após, o programa deverá conferir se a letra digitada está dentro da palavra secreta;
3) se estiver, o programa deverá exibir a letra;
4) se não estiver, o programa deverá exibir "*";
5) faça a contagem de tentativas que o usuário tentou.
"""

palavra_secreta: "tecnologia"

while True:
    letra_digitada = input("Digite uma letra de A a Z: ")
    if len(letra_digitada) > 1:
        print("Digite somente uma letra")
        continue
    
    print("O jogo continua")
    
    
    
    # letra in alfabeto: # percorre de A a Z
    # if letra == a:
    #         print("a letra está na palavra")
    #         continue
    # else:
    #     print("a letra não está na palavra")
    
    
   

