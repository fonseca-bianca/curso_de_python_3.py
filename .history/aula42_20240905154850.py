"""Iterando strings com while"""
# barra invertida = quebra de linha, MAS as "aspas" têm q colocar de novo na linha seguinte

frase = "O Python é uma LP"\
    "multiparadigma."\
    "Python foi criada por Guido von Rossum"
 
i = 0
qtd_vezes_letra = 0
letra_mais_vezes = " "

while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_letra_atual = frase.count(letra_atual)
    
    if qtd_vezes_letra < qtd_vezes_letra_atual:
        qtd_vezes_letra = qtd_vezes_letra_atual

    print(letra_atual, qtd_vezes_letra_atual) #vai aparecer a letra e ao lado a qntdade de vzs q ela apareceu. Espaço em branco tbm é caractere
    i += 1 # fecha a iteração pra NÃO entrar em um loop infinito