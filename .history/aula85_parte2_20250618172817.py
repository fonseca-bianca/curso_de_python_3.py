"""
List Comprehension com MAIS de um 'for':
"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
        
print(lista) 

