"""Métodos da STRING e LIST:
split: divide uma string
join: une uma string
strip: corta espaços início e fim string ou substring (divisão de duas ou mais strings) ou palavra
"""

frase = "Mas, olha só que coisa interessante. "

lista_palavras = frase.split(", ") 
#split(","): divide a string 'frase' em substrings qndo encontra a vírgula
#é como se ele cortasse da string o q queremos remover dela

print(lista_palavras)

for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].strip())

