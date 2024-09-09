"""Jogo palavra secreta
Usuário deverá adivinhar a palavra
1) usuário poderá digitar apenas 1 letra;
2) após, o programa deverá conferir se a letra digitada está dentro da palavra secreta;
3) se estiver, o programa deverá exibir a letra;
4) se não estiver, o programa deverá exibir "*";
5) faça a contagem de tentativas que o usuário tentou.
"""

palavra_secreta = "tecnologia"
letras_corretas = "" 
# letras corretas vão ser salvas dentro da string vazia 'letras_corretas'

while True:
    letra_digitada = input("Digite uma letra de A a Z: ")
    
    if len(letra_digitada) > 1:
        print("Digite somente uma letra")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    else:
        print(f"A letra '{letra_digitada}' não está na palavra secreta")
    
    # se a letra estiver na palvra secreta, então o programa vai exibir a letra. Essa letra será mantida
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            print(letra_secreta)
        # se a letra digitada não estiver na palavra secreta, então o programa vai exibir um '*'
        else:
            print("*") 
        

    
    
    
    
   

