"""Iterando strings com while"""
# barra invertida = quebra de linha, MAS as "aspas" têm q colocar de novo na linha seguinte

frase = "O Python é uma LP"\
    "multiparadigma."\
    "Python foi criada por Guido von Rossum"
 
i = 0

while i < len(frase):
    letra_atual = frase[i]
    quantidade_vezes_letra = frase.count(letra_atual)

    print(letra_atual, quantidade_vezes_letra)
    i += 1 # fecha a iteração pra NÃO entrar em um loop infinito