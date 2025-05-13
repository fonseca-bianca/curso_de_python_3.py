""" Métodos da STRING:
.split(): divide uma string (geralmente retorna uma list)
.join(): une uma string
.strip(): corta espaços início e fim string ou substring (divisão de duas 
ou mais strings) ou palavra
.lstrip(): corta espaços da esquerda
.rstring(): corta espaços da direita
"""

frase = " Mas olha só que coisa interessante. "
frase2 = "Hoje é sexta-feira 13!"

# .split():
lista_palavras = frase.split(", ") 
# divide string onde há vírgula seguida de espaço
# split(","): divide a string 'frase' em substrings qndo encontra a vírgula
# é como se ele cortasse da string o q queremos remover dela
print(lista_palavras)

# .strip():
for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].strip()) # remove vírgula e espaço em branco 
    # início e final
    
# .join(): informar na string qual o separador q irá utilizar
#   une os iteráveis (LIST, STRING, TUPLE) dentro dos parênteses
frase_unida = "*".join(frase2)
print(frase_unida)
