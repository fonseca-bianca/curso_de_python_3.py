""" 
Exemplo de uso do tipo SET:
O SET, em Python, facilita pra evitar a sobrecarga de espaço de armazenamento 
de dados no programa, já que NÃO salva itens repetidos.
Se, por ex., pedir pro usuário inserir algum dado e ele repetir, o SET irá armazenar
somente o primeiro e manter ele na memória.
"""

letras = set()
while True:
    letra = input("Digite a letra: ")
    letras.add(letra.lower())
    
    if "m" in letras:
        print("Parabéns! você encontrou a letra")
        break
    
    print(letras)