"""
List Comprehension com MAIS de um 'for':
"""

lista1 = []
for x in range(3):
    for y in range(3):
        lista1.append((x,y))
print(lista1)

print()

# nesse caso, tbm temos um 'for' dentro do 'for':
lista2 = [
    (x, y) # esse é o lado esquerdo do 'for' e é usado pro mapeamento
    for x in range(3)
    for y in range(3)
]

print(lista2)

# para cada 'x', ele vai iterar sobre cada letra da palavra 'Python':
# esta é uma List Comprehension dentro do valor de uma List Comprehension:
lista3 = [
    [letra for letra in 'Python'] # nível interno
    for x in range(1) # nível externo
]

print(lista3)

# OBS.: 'x' transparente na lista3:
#   Ele executa o que está dentro da list comprehension uma vez, mas não 
# participa diretamente do valor criado
#   Quando o interpretador ou IDE deixa ele “transparente” ou “cinza claro”, 
# isso indica: “variável declarada mas não utilizada”
# poderia substituir 'x' por '_' (underscore) para indicar que não será usado

