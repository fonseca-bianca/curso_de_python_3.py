"""While/else"""
# em Python, o while tem else
# quando o laço while é executado por completo, aí o laço else será executado
# OBS.: se der um 'break' no while, o else NÃO será executado

string = "Valor qualquer"

i = 0 # variável que irá funcionar como índice do loop

# loop 'while' irá continuar até que o índice 'i' seja menor que o comprimento da variável 'string'
while i < len(string):
    # a cada iteração do loop, a variável 'letra' armazena o caractere na posição 'i' da 'string'
    letra = string[i]
    
    print(letra)
    i += 1
else:
    print("O else foi executado")

print("Fora do bloco 'while'")