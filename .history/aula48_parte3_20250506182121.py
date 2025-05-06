"""
.insert():
    método q recebe 2 argumentos como parâmetros:
    - 1º: em qual índice você vai mexer;
    - 2º: qual o valor que você quer colocar
"""

minha_lista = [1, 2, 3, 4]
print(minha_lista[3]) # output: 4
minha_lista.append("Ana")
del minha_lista[2]
# minha_lista.clear()
minha_lista.insert(0, "João")
print(minha_lista)
print(minha_lista[2:4]) 
# A lista atual é ["João", 1, 2, 4, "Ana"], então:
#   Índice 2: 2
#   Índice 3: 4
#   Índice 4: "Ana" (não incluso no slice, pois o final é exclusivo).
# Portanto, o slice [2:4] retorna [2, 4]
# Se você quisesse incluir "Ana", deveria usar [2:5] 
# (já que a lista tem tamanho 5 agora), mas mesmo assim o resultado 
# seria [2, 4, "Ana"], não [2, "Ana"].
