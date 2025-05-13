"""Listas de listas e seus índices
"""

lord_of_rings = [
    #   0         1         
    ["Gendalf", "Sam"], # índice 0 da lista de dentro
    ["Sauron", "Galadriel", "Frodo"], # índice 1 da lista de dentro
    ["Piki", (0, 10, 20, 30, 40)] # índice 2 da lista de dentro
]

print(lord_of_rings[1][0]) # vai imprimir o índice 1 da lista de dentro e 
# de dentro da lista, o índice 0 = Sauron
print(lord_of_rings[0][1]) # Sam
print(lord_of_rings[2][0]) # Piki
print(lord_of_rings[2][1]) # imprime a tupla (0, 10, 20, 30, 40)
print(lord_of_rings[2][1][2]) # imprime o número 20 da tupla dentro da 
# lista de dentro da lista 'lord_of_rings'


#  variável lord dentro do loop for corresponde a cada uma das sublistas 
# dentro
# da lista lord_of_rings.
# lord será, em cada iteração, uma das listas aninhadas (internas) de 
# lord_of_rings

# 1º for: lista 'maior' = lord_of_rings
# 2º for: listas (0 a 2) 'menores' dentro da lista maior 
for lord in lord_of_rings: 
    print(f"O personagem é: {lord}") 
    for personagem in lord:
        print(personagem)
        
# Análise do uso de cada 'for':
# 1º for:
#     pra cada 'lord' em 'lord_of_rings', me retorne o valor de 'lord'
# 2º for:
#     pra cada 'personagem' em 'lord', me retorne o valor de 'personagem'