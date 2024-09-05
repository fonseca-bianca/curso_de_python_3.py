"""Iterando strings com while"""
# barra invertida = quebra de linha, MAS as "aspas" têm q colocar de novo na linha seguinte

frase = "O Python é uma LP"\
    "multiparadigma."\
    "Python foi criada por Guido von Rossum"
 
i = 0

while i < len(frase):
    letra_atual = frase[i]

    print(letra_atual)
    i += 1