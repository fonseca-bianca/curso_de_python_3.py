"""
List Comprehension com MAIS de um 'for':
"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

# nesse caso, tbm temos um 'for' dentro do 'for':
lista = [
    (x, y) # esse é o lado esquerdo do 'for' e é usado pro mapeamento
    for x in range(3)
    for y in range(3)
]

print(lista) 

