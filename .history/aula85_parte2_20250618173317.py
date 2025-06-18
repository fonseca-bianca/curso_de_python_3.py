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

