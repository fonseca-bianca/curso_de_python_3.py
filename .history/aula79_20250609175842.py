""" 
Exemplo de uso do tipo SET:
O SET, em Python, facilita pra evitar a sobrecarga de espaço de armazenamento 
de dados no programa, já que NÃO salva itens repetidos.
Se, por ex., pedir pro usuário inserir algum dado e ele repetir, o SET irá 
armazenar somente o primeiro e manter ele na memória.
"""

typed_letter = set()
while True:
    letter = input("Digite a letra: ")
    typed_letter.add(letter.lower()) # converte letra digitada pra minúscula
    
    if "m" in typed_letter:
        print("Parabéns! você encontrou a letra premiada \õ/")
        break
    else:
        print("Você ainda não encontrou a letra premiada :( "
              "Continue digitando até encontrá-la.")
    
    print(typed_letter)