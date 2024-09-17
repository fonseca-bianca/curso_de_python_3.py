"""Listas de listas e seus índices
"""

lord_of_rings = [
    ["Gendalf", "Sam"], # índice 0 da lista de dentro
    ["Sauron", "Galadriel", "Frodo"], # índice 1 da lista de dentro
    ["Piki", (0, 10, 20, 30, 40)] # índice 2 da lista de dentro
]

print(lord_of_rings[1][0]) # vai imprimir o índice 1 da lista de dentro e de dentro dela o índice 0 = Sauron
print(lord_of_rings[0][1]) # Sam
print(lord_of_rings[2][0]) # Piki
print(lord_of_rings[2][1][2]) # imprime o número 20 da tupla dentro da lista de dentro da lista 'lord_of_rings'


for lord in lord_of_rings:
    print(lord)