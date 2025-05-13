""" Métodos da STRING:
.split(): só separa a string quando encontra exatamente (vírgula e espaço)
(geralmente retorna uma list)
    OBS.:
        esse método NÃO altera a string original, se a string original NÃO
        tiver o separador, ele não vai fazer nada
    - usar SEM argumento ():
        ele vai preencher o espaço em branco entre as palavras com vírgula
    - usar COM argumento (separador q pode ser vírgula, espaço, etc):
        somente usar quando a string tiver o separador esse separador explícito
        dentro dela
.join(): une uma string
.strip(): corta espaços início e fim string ou substring (divisão de duas 
ou mais strings) ou palavra
.lstrip(): corta espaços da esquerda
.rstring(): corta espaços da direita
"""

frase1 = "   Mas olha só que coisa interessante. "
frase2 = "Hoje é sexta-feira 13!"
frase3 = "Eu#sou#dev#python#com#orgulho"
frase4 = "Eusouassimdesdecriança"
frase5 = "Eu sou programadora Python, amo o que faço!"
lista_letra_palavra = frase1

# .split():
lista_palavras = frase1.split() # SEM argumento
print(lista_palavras)
# output: ['Mas', 'olha', 'só', 'que', 'coisa', 'interessante.']

lista_palavras = frase3.split("#") # COM argumento
print(lista_palavras)
# output: ['Eu', 'sou', 'dev', 'python', 'com', 'orgulho']

lista_palavras = frase4.split(", ")
print(lista_palavras)

lista_palavras = frase5.split(",") 
# vai dividir a string onde há vírgula em duas partes (como se fosse 2 frases)
print(lista_palavras)

# divide string onde há vírgula seguida de espaço
# split(","): divide a string 'frase' em substrings qndo encontra a vírgula
# é como se ele cortasse da string o q queremos remover dela


# .strip():
for i, frase1 in enumerate(lista_letra_palavra):
    print(lista_letra_palavra.strip()) 
print(lista_letra_palavra[i])
    
    
# .join(): informar na string qual o separador q irá utilizar
#   une os iteráveis (LIST, STRING, TUPLE) dentro dos parênteses
frase_unida = "*".join(frase2)
print(frase_unida)
